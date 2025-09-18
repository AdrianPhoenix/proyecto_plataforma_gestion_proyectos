import React, { createContext, useContext, useEffect, useState } from 'react';
import type { User, AuthResponse } from '../types';
import type { LoginFormData, RegisterFormData } from '../utils/schemas';
import { authAPI } from '../services/api';

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (data: LoginFormData) => Promise<void>;
  register: (data: RegisterFormData) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

// Crear contexto de autenticación
const AuthContext = createContext<AuthContextType | undefined>(undefined);

/**
 * Hook personalizado para usar el contexto de autenticación.
 * Debe ser usado dentro de un AuthProvider.
 */
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

/**
 * Proveedor de contexto de autenticación.
 * Maneja el estado global de autenticación de la aplicación.
 */
export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // Verificar si hay un token guardado al cargar la aplicación
  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (token) {
      // Intentar obtener el perfil del usuario con el token guardado
      authAPI.getProfile()
        .then(setUser)
        .catch(() => {
          // Token inválido, limpiar storage
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  /**
   * Inicia sesión del usuario.
   * Guarda tokens en localStorage y actualiza el estado.
   */
  const login = async (data: LoginFormData) => {
    const response: AuthResponse = await authAPI.login(data);
    localStorage.setItem('access_token', response.access);
    localStorage.setItem('refresh_token', response.refresh);
    setUser(response.user);
  };

  /**
   * Registra un nuevo usuario.
   * Guarda tokens en localStorage y actualiza el estado.
   */
  const register = async (data: RegisterFormData) => {
    const response: AuthResponse = await authAPI.register(data);
    localStorage.setItem('access_token', response.access);
    localStorage.setItem('refresh_token', response.refresh);
    setUser(response.user);
  };

  /**
   * Cierra sesión del usuario.
   * Limpia tokens del localStorage y resetea el estado.
   */
  const logout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setUser(null);
  };

  const value = {
    user,
    loading,
    login,
    register,
    logout,
    isAuthenticated: !!user,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
