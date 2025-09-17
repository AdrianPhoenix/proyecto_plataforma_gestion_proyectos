import { useState } from 'react';
import { useTasks } from '../hooks/useTasks';
import TaskModal from '../components/TaskModal';
import TaskCommentsModal from '../components/TaskCommentsModal';
import type { Task } from '../types';
import type { TaskFormData } from '../utils/schemas';

const Tasks = () => {
  const { tasks, loading, error, createTask, updateTask, deleteTask, fetchMyTasks } = useTasks();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isCommentsModalOpen, setIsCommentsModalOpen] = useState(false);
  const [editingTask, setEditingTask] = useState<Task | undefined>();
  const [selectedTask, setSelectedTask] = useState<Task | undefined>();
  const [showMyTasks, setShowMyTasks] = useState(false);

  const handleCreateTask = async (data: TaskFormData) => {
    await createTask(data);
  };

  const handleUpdateTask = async (data: TaskFormData) => {
    if (editingTask) {
      await updateTask(editingTask.id, data);
      setEditingTask(undefined);
    }
  };

  const handleDeleteTask = async (id: number) => {
    if (confirm('¿Estás seguro de que quieres eliminar esta tarea?')) {
      await deleteTask(id);
    }
  };

  const openCreateModal = () => {
    setEditingTask(undefined);
    setIsModalOpen(true);
  };

  const openEditModal = (task: Task) => {
    setEditingTask(task);
    setIsModalOpen(true);
  };

  const openCommentsModal = (task: Task) => {
    setSelectedTask(task);
    setIsCommentsModalOpen(true);
  };

  const toggleMyTasks = () => {
    setShowMyTasks(!showMyTasks);
    if (!showMyTasks) {
      fetchMyTasks();
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'pending': return 'bg-yellow-100 text-yellow-800';
      case 'in_progress': return 'bg-blue-100 text-blue-800';
      case 'completed': return 'bg-green-100 text-green-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const getStatusText = (status: string) => {
    switch (status) {
      case 'pending': return 'Pendiente';
      case 'in_progress': return 'En Progreso';
      case 'completed': return 'Completado';
      default: return status;
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="sm:flex sm:items-center">
        <div className="sm:flex-auto">
          <h1 className="text-xl font-semibold text-gray-900">
            {showMyTasks ? 'Mis Tareas' : 'Todas las Tareas'}
          </h1>
          <p className="mt-2 text-sm text-gray-700">
            {showMyTasks 
              ? 'Lista de tareas asignadas a ti.' 
              : 'Lista de todas las tareas de los proyectos.'
            }
          </p>
        </div>
        <div className="mt-4 sm:mt-0 sm:ml-16 sm:flex-none space-x-3">
          <button
            onClick={toggleMyTasks}
            className="inline-flex items-center justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50"
          >
            {showMyTasks ? 'Ver Todas' : 'Mis Tareas'}
          </button>
          <button
            onClick={openCreateModal}
            className="inline-flex items-center justify-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700"
          >
            Nueva Tarea
          </button>
        </div>
      </div>

      {error && (
        <div className="mt-4 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      )}

      <div className="mt-8 bg-white shadow rounded-lg overflow-hidden">
        {tasks.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500">No hay tareas disponibles.</p>
            <p className="text-sm text-gray-400 mt-2">
              {showMyTasks 
                ? 'No tienes tareas asignadas.' 
                : 'Crea tu primera tarea para comenzar.'
              }
            </p>
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Tarea
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Proyecto
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Estado
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Asignado a
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Vencimiento
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Acciones
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {tasks.map((task) => (
                  <tr key={task.id}>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div>
                        <div className="text-sm font-medium text-gray-900">
                          {task.name}
                        </div>
                        <div className="text-sm text-gray-500">
                          {task.description}
                        </div>
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {task.project_name}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getStatusColor(task.status)}`}>
                        {getStatusText(task.status)}
                      </span>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {task.assigned_to ? task.assigned_to.username : 'Sin asignar'}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {new Date(task.due_date).toLocaleDateString()}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                      <button
                        onClick={() => openCommentsModal(task)}
                        className="text-indigo-600 hover:text-indigo-900 mr-4"
                      >
                        Comentarios ({task.comments_count || 0})
                      </button>
                      <button
                        onClick={() => openEditModal(task)}
                        className="text-blue-600 hover:text-blue-900 mr-4"
                      >
                        Editar
                      </button>
                      <button
                        onClick={() => handleDeleteTask(task.id)}
                        className="text-red-600 hover:text-red-900"
                      >
                        Eliminar
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      <TaskModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSubmit={editingTask ? handleUpdateTask : handleCreateTask}
        task={editingTask}
        title={editingTask ? 'Editar Tarea' : 'Nueva Tarea'}
      />

      {selectedTask && (
        <TaskCommentsModal
          isOpen={isCommentsModalOpen}
          onClose={() => setIsCommentsModalOpen(false)}
          task={selectedTask}
        />
      )}
    </div>
  );
};

export default Tasks;
