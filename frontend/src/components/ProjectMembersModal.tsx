import { useState, useEffect } from 'react';
import { projectsAPI, authAPI } from '../services/api';
import type { Project, User } from '../types';

interface ProjectMembersModalProps {
  isOpen: boolean;
  onClose: () => void;
  project: Project;
  onUpdate: () => void;
}

const ProjectMembersModal = ({ isOpen, onClose, project, onUpdate }: ProjectMembersModalProps) => {
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUser, setSelectedUser] = useState<number | ''>('');
  const [selectedRole, setSelectedRole] = useState<'admin' | 'collaborator' | 'viewer'>('viewer');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (isOpen) {
      authAPI.getUsers().then(setUsers);
    }
  }, [isOpen]);

  const handleAddMember = async () => {
    if (!selectedUser) return;
    
    setLoading(true);
    try {
      await projectsAPI.addMember(project.id, Number(selectedUser), selectedRole);
      setSelectedUser('');
      setSelectedRole('viewer');
      onUpdate();
    } catch (error) {
      console.error('Error adding member:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleRemoveMember = async (memberId: number) => {
    if (!confirm('¿Eliminar este miembro del proyecto?')) return;
    
    try {
      await projectsAPI.removeMember(project.id, memberId);
      onUpdate();
    } catch (error) {
      console.error('Error removing member:', error);
    }
  };

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

  if (!isOpen) return null;

  const availableUsers = Array.isArray(users) ? users.filter(user => 
    !(project.members || []).some(member => member.user.id === user.id)
  ) : [];

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-2xl max-h-[80vh] overflow-hidden">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-gray-200">
          <h2 className="text-xl font-semibold text-gray-900 flex items-center">
            <svg className="w-6 h-6 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z" />
            </svg>
            Miembros del Proyecto
          </h2>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 transition-colors"
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div className="p-6 max-h-96 overflow-y-auto">
          {/* Add Member Form */}
          <div className="mb-6 p-4 bg-gray-50 rounded-lg">
            <h3 className="text-sm font-medium text-gray-900 mb-3">Agregar Miembro</h3>
            <div className="flex gap-3">
              <select
                value={selectedUser}
                onChange={(e) => setSelectedUser(e.target.value === '' ? '' : Number(e.target.value))}
                className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-white text-gray-900"
              >
                <option value="">Seleccionar usuario</option>
                {availableUsers.map((user) => (
                  <option key={user.id} value={user.id}>
                    {user.username} ({user.email})
                  </option>
                ))}
              </select>
              <select
                value={selectedRole}
                onChange={(e) => setSelectedRole(e.target.value as any)}
                className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 bg-white text-gray-900"
              >
                <option value="viewer">Visor</option>
                <option value="collaborator">Colaborador</option>
                <option value="admin">Administrador</option>
              </select>
              <button
                onClick={handleAddMember}
                disabled={!selectedUser || loading}
                className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? 'Agregando...' : 'Agregar'}
              </button>
            </div>
          </div>

          {/* Members List */}
          <div>
            <h3 className="text-sm font-medium text-gray-900 mb-3">
              Miembros Actuales ({project.members?.length || 0})
            </h3>
            <div className="space-y-3">
              {(project.members || []).map((member) => (
                <div key={member.id} className="flex items-center justify-between p-3 bg-white border border-gray-200 rounded-lg">
                  <div className="flex items-center space-x-3">
                    <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
                      <span className="text-white font-semibold text-sm">
                        {member.user.username.charAt(0).toUpperCase()}
                      </span>
                    </div>
                    <div>
                      <p className="font-medium text-gray-900">{member.user.username}</p>
                      <p className="text-sm text-gray-500">{member.user.email}</p>
                    </div>
                  </div>
                  <div className="flex items-center space-x-3">
                    <span className={`px-2 py-1 text-xs font-medium rounded-full ${getRoleColor(member.role)}`}>
                      {getRoleText(member.role)}
                    </span>
                    <button
                      onClick={() => handleRemoveMember(member.id)}
                      className="text-red-600 hover:text-red-800 p-1"
                    >
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                      </svg>
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="flex justify-end p-6 border-t border-gray-200">
          <button
            onClick={onClose}
            className="px-4 py-2 text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-lg transition-colors"
          >
            Cerrar
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProjectMembersModal;
