import { useState } from "react";

import {
  Box,
  Button,
} from "@mui/material";

import SnackbarMessage from "@/shared/components/SnackbarMessage";

import { useCategorias } from "@/modules/catalogos/categorias/hooks/useCategorias";

import ImplementosTable from "@/modules/implementos/components/ImplementosTable";
import NuevoImplementoDialog from "@/modules/implementos/components/NuevoImplementoDialog";

import { useImplementos } from "@/modules/implementos/hooks/useImplementos";
import { useCrearImplemento } from "@/modules/implementos/hooks/useCrearImplemento";

import type { ImplementoFormData } from "@/modules/implementos/schemas/implementoSchema";

import PageHeader from "@/shared/components/PageHeader";

export default function ImplementosPage() {
  const [dialogOpen, setDialogOpen] = useState(false);

  const [snackbarOpen, setSnackbarOpen] =
    useState(false);

  const [snackbarMessage, setSnackbarMessage] =
    useState("");

  const [snackbarSeverity, setSnackbarSeverity] =
    useState<"success" | "error">("success");

  const {
    data: implementos = [],
    isLoading,
    isError,
  } = useImplementos();

  const {
    data: categorias = [],
  } = useCategorias();

  const crearImplemento =
    useCrearImplemento();

  async function guardarImplemento(
    datos: ImplementoFormData,
  ) {
    try {
      await crearImplemento.mutateAsync(
        datos,
      );

      setDialogOpen(false);

      setSnackbarSeverity("success");

      setSnackbarMessage(
        "Implemento registrado correctamente.",
      );

      setSnackbarOpen(true);

    } catch {

      setSnackbarSeverity("error");

      setSnackbarMessage(
        "No fue posible registrar el implemento.",
      );

      setSnackbarOpen(true);
    }
  }

  console.log({
    implementos,
    isLoading,
    isError,
    categorias,
    crearPendiente: crearImplemento.isPending,
  });

  return (
    <Box
      sx={{
        p: 4,
      }}
    >
      <PageHeader
  title="Implementos"
  backTo="/dashboard"
  action={
    <Button
      variant="contained"
      onClick={() => setDialogOpen(true)}
    >
      Nuevo Implemento
    </Button>
  }
/>

      <ImplementosTable
        rows={implementos}
        loading={isLoading}
        error={isError}
      />

      <NuevoImplementoDialog
        open={dialogOpen}
        onClose={() =>
          setDialogOpen(false)
        }
        categorias={categorias}
        onGuardar={guardarImplemento}
        loading={
          crearImplemento.isPending
        }
      />

      <SnackbarMessage
        open={snackbarOpen}
        message={snackbarMessage}
        severity={snackbarSeverity}
        onClose={() =>
          setSnackbarOpen(false)
        }
      />
    </Box>
  );
}