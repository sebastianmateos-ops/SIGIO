import { useState } from "react";

import {
  Box,
  Button,
  Stack,
  Typography,
} from "@mui/material";

import SnackbarMessage from "@/shared/components/SnackbarMessage";

import { useCategorias } from "@/modules/catalogos/categorias/hooks/useCategorias";

import ImplementosTable from "@/modules/implementos/components/ImplementosTable";
import NuevoImplementoDialog from "@/modules/implementos/components/NuevoImplementoDialog";

import { useImplementos } from "@/modules/implementos/hooks/useImplementos";
import { useCrearImplemento } from "@/modules/implementos/hooks/useCrearImplemento";

import type { ImplementoFormData } from "@/modules/implementos/schemas/implementoSchema";

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

  return (
    <Box
      sx={{
        p: 4,
      }}
    >
      <Stack
        direction="row"
        sx={{
          mb: 4,
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <Typography variant="h4">
          Implementos
        </Typography>

        <Button
          variant="contained"
          onClick={() =>
            setDialogOpen(true)
          }
        >
          Nuevo Implemento
        </Button>
      </Stack>

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