import { Navigate, Route, Routes } from "react-router-dom";

import { useAuth } from "../contexts/AuthContext";

import LoginPage from "../pages/LoginPage";
import DashboardPage from "../pages/DashboardPage";
import NotFoundPage from "../pages/NotFoundPage";

import ProtectedRoute from "./ProtectedRoute";

import ImplementosPage from "../modules/implementos/pages/ImplementosPage";
import BeneficiariosPage from "../modules/beneficiarios/pages/BeneficiariosPage";
import PrestamosPage from "../modules/prestamos/pages/PrestamosPage";

export default function AppRouter() {
  const { isAuthenticated } = useAuth();

  return (
    <Routes>
      <Route
        path="/"
        element={
          isAuthenticated ? (
            <Navigate to="/dashboard" replace />
          ) : (
            <LoginPage />
          )
        }
      />

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <DashboardPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/implementos"
        element={
          <ProtectedRoute>
            <ImplementosPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/beneficiarios"
        element={
          <ProtectedRoute>
            <BeneficiariosPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/prestamos"
        element={
          <ProtectedRoute>
            <PrestamosPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="*"
        element={<NotFoundPage />}
      />

    </Routes>
  );
}