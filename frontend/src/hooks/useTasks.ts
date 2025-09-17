import { useState, useEffect } from 'react';
import { tasksAPI } from '../services/api';
import type { Task } from '../types';
import type { TaskFormData } from '../utils/schemas';

export const useTasks = (projectId?: number) => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const data = await tasksAPI.getTasks(projectId);
      setTasks(Array.isArray(data) ? data : []);
      setError(null);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error al cargar tareas');
      setTasks([]);
    } finally {
      setLoading(false);
    }
  };

  const fetchMyTasks = async () => {
    try {
      setLoading(true);
      const data = await tasksAPI.getMyTasks();
      setTasks(Array.isArray(data) ? data : []);
      setError(null);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error al cargar mis tareas');
      setTasks([]);
    } finally {
      setLoading(false);
    }
  };

  const createTask = async (data: TaskFormData) => {
    const newTask = await tasksAPI.createTask(data);
    setTasks(prev => [...prev, newTask]);
    return newTask;
  };

  const updateTask = async (id: number, data: Partial<TaskFormData>) => {
    const updatedTask = await tasksAPI.updateTask(id, data);
    setTasks(prev => prev.map(t => t.id === id ? updatedTask : t));
    return updatedTask;
  };

  const deleteTask = async (id: number) => {
    await tasksAPI.deleteTask(id);
    setTasks(prev => prev.filter(t => t.id !== id));
  };

  useEffect(() => {
    fetchTasks();
  }, [projectId]);

  return {
    tasks,
    loading,
    error,
    fetchTasks,
    fetchMyTasks,
    createTask,
    updateTask,
    deleteTask,
  };
};
