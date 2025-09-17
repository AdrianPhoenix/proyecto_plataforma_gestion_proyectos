import { useState, useEffect } from 'react';
import { projectsAPI } from '../services/api';
import type { Project } from '../types';
import type { ProjectFormData } from '../utils/schemas';

export const useProjects = () => {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchProjects = async () => {
    try {
      setLoading(true);
      const data = await projectsAPI.getProjects();
      setProjects(Array.isArray(data) ? data : []);
      setError(null);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error al cargar proyectos');
      setProjects([]);
    } finally {
      setLoading(false);
    }
  };

  const createProject = async (data: ProjectFormData) => {
    const newProject = await projectsAPI.createProject(data);
    setProjects(prev => [...prev, newProject]);
    return newProject;
  };

  const updateProject = async (id: number, data: Partial<ProjectFormData>) => {
    const updatedProject = await projectsAPI.updateProject(id, data);
    setProjects(prev => prev.map(p => p.id === id ? updatedProject : p));
    return updatedProject;
  };

  const deleteProject = async (id: number) => {
    await projectsAPI.deleteProject(id);
    setProjects(prev => prev.filter(p => p.id !== id));
  };

  useEffect(() => {
    fetchProjects();
  }, []);

  return {
    projects,
    loading,
    error,
    fetchProjects,
    createProject,
    updateProject,
    deleteProject,
  };
};
