import { useState } from "react";

import {
  Box,
  Button,
} from "@mui/material";

import PageHeader from "@/shared/components/PageHeader";
import SnackbarMessage from "@/shared/components/SnackbarMessage";

import PrestamosTable from "../components/PrestamosTable";
import NuevoPrestamoDialog from "../components/NuevoPrestamoDialog";
import DevolverPrestamoDialog from "../components/DevolverPrestamoDialog";

import { usePrestamos } from "../hooks/usePrestamos";
import { useCrearPrestamo } from "../hooks/useCrearPrestamo";
import { useDevolverPrestamo } from "../hooks/useDevolverPrestamo";

import { useImplementos } from "@/modules/implementos/hooks/useImplementos";
import { useBeneficiarios } from "@/modules/beneficiarios/hooks/useBeneficiarios";

import type {
  Prestamo,
  PrestamoUpdate,
} from "@/modules/prestamos/services/prestamoService";

import type { PrestamoFormData } from "../schemas/prestamoSchema";

export default function PrestamosPage() {
  const [dialogOpen, setDialogOpen] = useState(false);

  const [dialogDevolucionOpen, setDialogDevolucionOpen] =
    useState(false);

  const [prestamoSeleccionado, setPrestamoSeleccionado] =
    useState<Prestamo | null>(null);

  const [snackbarOpen, setSnackbarOpen] =
    useState(false);

  const [snackbarMessage, setSnackbarMessage] =
    useState("");

  const [snackbarSeverity, setSnackbarSeverity] =
    useState<"success" | "error">("success");

  const {
    data: prestamos = [],
    isLoading,
    isError,
  } = usePrestamos();

  const {
    data: implementos = [],
  } = useImplementos();

  const {
    data: beneficiarios = [],
  } = useBeneficiarios();

  const implementosDisponibles =
    implementos.filter(
      (implemento) =>
        implemento.estado === "Disponible",
    );

  const crearPrestamo =
    useCrearPrestamo();

  const devolverPrestamo =
    useDevolverPrestamo();

  async function guardarPrestamo(
    datos: PrestamoFormData,
  ) {
    try {
      await crearPrestamo.mutateAsync(datos);

      setDialogOpen(false);

      setSnackbarSeverity("success");
      setSnackbarMessage(
        "Préstamo registrado correctamente.",
      );
      setSnackbarOpen(true);

    } catch {

      setSnackbarSeverity("error");
      setSnackbarMessage(
        "No fue posible registrar el préstamo.",
      );
      setSnackbarOpen(true);
    }
  }

  function handleDevolver(
    prestamo: Prestamo,
  ) {
    setPrestamoSeleccionado(prestamo);
    setDialogDevolucionOpen(true);
  }

  async function confirmarDevolucion(
    observaciones: string,
  ) {
    if (!prestamoSeleccionado) return;

    const datos: PrestamoUpdate = {
      fecha_devolucion: new Date().toISOString(),
      observaciones,
    };

    try {
      await devolverPrestamo.mutateAsync({
        id: prestamoSeleccionado.id,
        datos,
      } as any);

      setDialogDevolucionOpen(false);
      setPrestamoSeleccionado(null);

      setSnackbarSeverity("success");
      setSnackbarMessage(
        "Devolución registrada correctamente.",
      );
      setSnackbarOpen(true);

    } catch {

      setSnackbarSeverity("error");
      setSnackbarMessage(
        "No fue posible registrar la devolución.",
      );
      setSnackbarOpen(true);
    }
  }

  return (
    <Box sx={{ p: 4 }}>
      <PageHeader
        title="Préstamos"
        backTo="/dashboard"
        action={
          <Button
            variant="contained"
            onClick={() => setDialogOpen(true)}
          >
            Nuevo Préstamo
          </Button>
        }
      />

      <PrestamosTable
        rows={prestamos}
        loading={isLoading}
        error={isError}
        onDevolver={handleDevolver}
      />

      <NuevoPrestamoDialog
        open={dialogOpen}
        onClose={() => setDialogOpen(false)}
        implementos={implementosDisponibles}
        beneficiarios={beneficiarios}
        onGuardar={guardarPrestamo}
        loading={crearPrestamo.isPending}
      />

      <DevolverPrestamoDialog
        open={dialogDevolucionOpen}
        onClose={() => {
          setDialogDevolucionOpen(false);
          setPrestamoSeleccionado(null);
        }}
        onConfirm={confirmarDevolucion}
        loading={devolverPrestamo.isPending}
      />

      <SnackbarMessage
        open={snackbarOpen}
        message={snackbarMessage}
        severity={snackbarSeverity}
        onClose={() => setSnackbarOpen(false)}
      />
    </Box>
  );
}