import { useState } from "react";

import {
  Box,
  Button,
} from "@mui/material";

import PageHeader from "@/shared/components/PageHeader";
import SnackbarMessage from "@/shared/components/SnackbarMessage";

import BeneficiariosTable from "../components/BeneficiariosTable";
import NuevoBeneficiarioDialog from "../components/NuevoBeneficiarioDialog";

import { useBeneficiarios } from "../hooks/useBeneficiarios";
import { useCrearBeneficiario } from "../hooks/useCrearBeneficiario";

import type { BeneficiarioFormData } from "../schemas/beneficiarioSchema";

export default function BeneficiariosPage() {
  const [dialogOpen, setDialogOpen] =
    useState(false);

  const [snackbarOpen, setSnackbarOpen] =
    useState(false);

  const [snackbarMessage, setSnackbarMessage] =
    useState("");

  const [snackbarSeverity, setSnackbarSeverity] =
    useState<"success" | "error">("success");

  const {
    data: beneficiarios = [],
    isLoading,
    isError,
  } = useBeneficiarios();

  const crearBeneficiario =
    useCrearBeneficiario();

  async function guardarBeneficiario(
    datos: BeneficiarioFormData,
  ) {
    try {
      await crearBeneficiario.mutateAsync(
        datos,
      );

      setDialogOpen(false);

      setSnackbarSeverity("success");

      setSnackbarMessage(
        "Beneficiario registrado correctamente.",
      );

      setSnackbarOpen(true);

    } catch {

      setSnackbarSeverity("error");

      setSnackbarMessage(
        "No fue posible registrar el beneficiario.",
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
      <PageHeader
        title="Beneficiarios"
        backTo="/dashboard"
        action={
          <Button
            variant="contained"
            onClick={() =>
              setDialogOpen(true)
            }
          >
            Nuevo Beneficiario
          </Button>
        }
      />

      <BeneficiariosTable
        rows={beneficiarios}
        loading={isLoading}
        error={isError}
      />

      <NuevoBeneficiarioDialog
        open={dialogOpen}
        onClose={() =>
          setDialogOpen(false)
        }
        loading={
          crearBeneficiario.isPending
        }
        onGuardar={
          guardarBeneficiario
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