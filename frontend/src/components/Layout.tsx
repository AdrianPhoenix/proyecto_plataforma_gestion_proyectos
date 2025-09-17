import { Outlet, Link, useLocation } from 'react-router-dom';
import { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import NotificationBell from './NotificationBell';

const Layout = () => {
  const { user, logout } = useAuth();
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const navigation = [
    { 
      name: 'Dashboard', 
      href: '/dashboard', 
      icon: (
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2H5a2 2 0 00-2-2z" />
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 5a2 2 0 012-2h4a2 2 0 012 2v6a2 2 0 01-2 2H10a2 2 0 01-2-2V5z" />
        </svg>
      )
    },
    { 
      name: 'Proyectos', 
      href: '/projects', 
      icon: (
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
        </svg>
      )
    },
    { 
      name: 'Tareas', 
      href: '/tasks', 
      icon: (
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
        </svg>
      )
    },
  ];

  const getRoleColor = (role: string) => {
    switch (role) {
      case 'admin': return 'bg-purple-100 text-purple-800';
      case 'collaborator': return 'bg-blue-100 text-blue-800';
      case 'viewer': return 'bg-green-100 text-green-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const getRoleText = (role: string) => {
    switch (role) {
      case 'admin': return 'Administrador';
      case 'collaborator': return 'Colaborador';
      case 'viewer': return 'Visor';
      default: return role;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {/* Sidebar */}
      <div className={`${sidebarOpen ? 'translate-x-0' : '-translate-x-full'} fixed inset-y-0 left-0 z-50 w-72 bg-gradient-to-b from-gray-900 via-gray-800 to-gray-900 shadow-2xl transform transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static lg:inset-0 flex flex-col`}>
        {/* Logo/Brand */}
        <div className="flex items-center justify-center h-20 px-6 border-b border-gray-700/50 flex-shrink-0">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg">
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
              </svg>
            </div>
            <div>
              <h1 className="text-xl font-bold text-white">ProjectHub</h1>
              <p className="text-xs text-gray-400">Gestión de Proyectos</p>
            </div>
          </div>
        </div>
        
        {/* Navigation */}
        <nav className="flex-1 px-6 py-8">
          <div className="space-y-1">
            {navigation.map((item) => (
              <Link
                key={item.name}
                to={item.href}
                className={`${
                  location.pathname === item.href
                    ? 'bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg'
                    : 'text-gray-300 hover:text-white hover:bg-gray-700/30'
                } group flex items-center px-3 py-3.5 text-sm font-medium rounded-lg transition-all duration-200`}
                onClick={() => setSidebarOpen(false)}
              >
                <span className={`mr-3 p-1.5 rounded-md ${
                  location.pathname === item.href 
                    ? 'bg-white/20' 
                    : 'bg-gray-700/30 group-hover:bg-gray-600/40'
                } transition-colors duration-200`}>
                  {item.icon}
                </span>
                <span className="font-medium tracking-wide">{item.name}</span>
                {location.pathname === item.href && (
                  <div className="ml-auto">
                    <div className="w-1.5 h-1.5 bg-white rounded-full animate-pulse"></div>
                  </div>
                )}
              </Link>
            ))}
          </div>
        </nav>

        {/* Quick Stats */}
        <div className="px-6 pb-6 flex-shrink-0">
          <div className="p-5 bg-gray-800/40 rounded-lg border border-gray-700/30">
            <h3 className="text-sm font-semibold text-gray-200 mb-4">Resumen Rápido</h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-xs text-gray-400">Proyectos</span>
                <span className="text-sm text-indigo-400 font-bold">0</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-xs text-gray-400">Tareas</span>
                <span className="text-sm text-emerald-400 font-bold">0</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-xs text-gray-400">Pendientes</span>
                <span className="text-sm text-amber-400 font-bold">0</span>
              </div>
            </div>
          </div>
        </div>

        {/* User Profile */}
        <div className="p-6 border-t border-gray-700/50 bg-gray-800/30 backdrop-blur-sm flex-shrink-0">
          <div className="flex items-center space-x-4 mb-5">
            <div className="relative">
              <div className="w-11 h-11 bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 rounded-full flex items-center justify-center shadow-lg ring-2 ring-gray-700">
                <span className="text-white font-bold text-base">
                  {user?.username?.charAt(0).toUpperCase()}
                </span>
              </div>
              <div className="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 bg-emerald-500 rounded-full border-2 border-gray-800"></div>
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-sm font-semibold text-white truncate">
                {user?.first_name || user?.username}
              </p>
              <p className="text-xs text-gray-400 truncate mb-1">
                {user?.email}
              </p>
              <span className={`inline-flex items-center px-2 py-0.5 text-xs font-medium rounded-full ${getRoleColor(user?.role || '')}`}>
                <div className="w-1.5 h-1.5 rounded-full bg-current mr-1"></div>
                {getRoleText(user?.role || '')}
              </span>
            </div>
          </div>
          
          <button
            onClick={logout}
            className="w-full bg-gradient-to-r from-red-600 to-red-700 hover:from-red-700 hover:to-red-800 text-white px-4 py-2.5 rounded-lg text-sm font-medium transition-all duration-200 flex items-center justify-center shadow-md hover:shadow-lg"
          >
            <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
            Cerrar Sesión
          </button>
        </div>
      </div>

      {/* Overlay for mobile */}
      {sidebarOpen && (
        <div 
          className="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      {/* Main content */}
      <div className="flex-1 flex flex-col lg:ml-0">
        {/* Top bar */}
        <div className="bg-white shadow-sm border-b border-gray-200 lg:hidden">
          <div className="flex items-center justify-between h-16 px-4">
            <button
              onClick={() => setSidebarOpen(true)}
              className="text-gray-500 hover:text-gray-700"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
            <h1 className="text-lg font-semibold text-gray-900">ProjectHub</h1>
            <NotificationBell />
          </div>
        </div>

        {/* Desktop notification bar */}
        <div className="hidden lg:block bg-white shadow-sm border-b border-gray-200">
          <div className="flex items-center justify-end h-16 px-6">
            <NotificationBell />
          </div>
        </div>

        {/* Page content */}
        <main className="flex-1 overflow-y-auto">
          <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
            <Outlet />
          </div>
        </main>
      </div>
    </div>
  );
};

export default Layout;
