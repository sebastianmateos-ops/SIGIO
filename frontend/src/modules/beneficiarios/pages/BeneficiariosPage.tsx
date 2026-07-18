import { useState } from "react";

import {
  Box,
  Button,
} from "@mui/material";

import PageHeader from "@/shared/components/PageHeader";
import SnackbarMessage from "@/shared/components/SnackbarMessage";
import ConfirmDialog from "@/shared/components/ConfirmDialog";
import SearchField from "@/shared/components/SearchField";

import BeneficiariosTable from "../components/BeneficiariosTable";
import NuevoBeneficiarioDialog from "../components/NuevoBeneficiarioDialog";
import EditarBeneficiarioDialog from "../components/EditarBeneficiarioDialog";
import VerBeneficiarioDialog from "../components/VerBeneficiarioDialog";

import { useBeneficiarios } from "../hooks/useBeneficiarios";
import { useCrearBeneficiario } from "../hooks/useCrearBeneficiario";
import { useActualizarBeneficiario } from "../hooks/useActualizarBeneficiario";
import { useDesactivarBeneficiario } from "../hooks/useDesactivarBeneficiario";
import { useBuscarBeneficiarios } from "../hooks/useBuscarBeneficiarios";

import type { Beneficiario } from "../types/beneficiario";

import type {
  BeneficiarioFormData,
} from "../schemas/beneficiarioSchema";

export default function BeneficiariosPage() {

  const [dialogOpen, setDialogOpen] =
    useState(false);

  const [searchText, setSearchText] =
    useState("");

  const [
    editarDialogOpen,
    setEditarDialogOpen,
  ] = useState(false);

  const [
    verDialogOpen,
    setVerDialogOpen,
  ] = useState(false);

  const [
    confirmDialogOpen,
    setConfirmDialogOpen,
    ] = useState(false);

  const [
    beneficiarioSeleccionado,
    setBeneficiarioSeleccionado,
  ] =
    useState<Beneficiario | null>(
      null,
    );

  const [
    snackbarOpen,
    setSnackbarOpen,
  ] = useState(false);

  const [
    snackbarMessage,
    setSnackbarMessage,
  ] = useState("");

  const [
    snackbarSeverity,
    setSnackbarSeverity,
  ] =
    useState<
      "success" | "error"
    >("success");

  const {
    data: beneficiarios = [],
    isLoading,
    isError,
  } = useBeneficiarios();

  const {
    data: resultadoBusqueda = [],
    } = useBuscarBeneficiarios(
    searchText,
  );

  const beneficiariosMostrados =
  searchText.trim().length >= 2
    ? resultadoBusqueda
    : beneficiarios;

  const crearBeneficiario =
    useCrearBeneficiario();

  const actualizarBeneficiario =
    useActualizarBeneficiario();

  const desactivarBeneficiario =
    useDesactivarBeneficiario();

  async function guardarBeneficiario(
    datos: BeneficiarioFormData,
  ) {

    try {

      await crearBeneficiario.mutateAsync(
        datos,
      );

      setDialogOpen(false);

      setSnackbarSeverity(
        "success",
      );

      setSnackbarMessage(
        "Beneficiario registrado correctamente.",
      );

      setSnackbarOpen(true);

    } catch {

      setSnackbarSeverity(
        "error",
      );

      setSnackbarMessage(
        "No fue posible registrar el beneficiario.",
      );

      setSnackbarOpen(true);

    }

  }

  async function editarBeneficiario(
    datos: BeneficiarioFormData,
  ) {

    if (!beneficiarioSeleccionado) {
      return;
    }

    try {

      await actualizarBeneficiario.mutateAsync(
        {
          id: beneficiarioSeleccionado.id,
          datos,
        },
      );

      setEditarDialogOpen(false);

      setBeneficiarioSeleccionado(
        null,
      );

      setSnackbarSeverity(
        "success",
      );

      setSnackbarMessage(
        "Beneficiario actualizado correctamente.",
      );

      setSnackbarOpen(true);

    } catch {

      setSnackbarSeverity(
        "error",
      );

      setSnackbarMessage(
        "No fue posible actualizar el beneficiario.",
      );

      setSnackbarOpen(true);

    }

  }

  function abrirEditar(
    beneficiario: Beneficiario,
  ) {

    setBeneficiarioSeleccionado(
      beneficiario,
    );

    setEditarDialogOpen(true);

  }

  function abrirVer(
    beneficiario: Beneficiario,
  ) {

    setBeneficiarioSeleccionado(
      beneficiario,
    );

    setVerDialogOpen(true);

  }

  function abrirDesactivar(
  beneficiario: Beneficiario,
) {

  setBeneficiarioSeleccionado(
    beneficiario,
  );

  setConfirmDialogOpen(true);

}

async function confirmarDesactivar() {

  if (!beneficiarioSeleccionado) {
    return;
  }

  try {

    await desactivarBeneficiario.mutateAsync(
      beneficiarioSeleccionado.id,
    );

    setConfirmDialogOpen(false);

    setBeneficiarioSeleccionado(
      null,
    );

    setSnackbarSeverity(
      "success",
    );

    setSnackbarMessage(
      "Beneficiario desactivado correctamente.",
    );

    setSnackbarOpen(true);

  } catch {

    setSnackbarSeverity(
      "error",
    );

    setSnackbarMessage(
      "No fue posible desactivar el beneficiario.",
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

      <Box
  sx={{
    mb: 3,
  }}
>
  <SearchField
    value={searchText}
    onChange={setSearchText}
    placeholder="Buscar por código, nombre, apellido o documento..."
  />
</Box>

      <BeneficiariosTable
        rows={beneficiariosMostrados}
        loading={isLoading}
        error={isError}
        onEditar={abrirEditar}
        onVer={abrirVer}
        onDesactivar={abrirDesactivar}
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

      <EditarBeneficiarioDialog
        open={editarDialogOpen}
        onClose={() => {

          setEditarDialogOpen(
            false,
          );

          setBeneficiarioSeleccionado(
            null,
          );

        }}
        beneficiario={
          beneficiarioSeleccionado
        }
        loading={
          actualizarBeneficiario.isPending
        }
        onGuardar={
          editarBeneficiario
        }
      />

      <VerBeneficiarioDialog
        open={verDialogOpen}
        beneficiario={
          beneficiarioSeleccionado
        }
        onClose={() => {

          setVerDialogOpen(
            false,
          );

          setBeneficiarioSeleccionado(
            null,
          );

        }}
      />

      <ConfirmDialog
        open={confirmDialogOpen}
        title="Desactivar beneficiario"
        message="¿Está seguro de que desea desactivar este beneficiario?"
        confirmText="Desactivar"
        cancelText="Cancelar"
        loading={
            desactivarBeneficiario.isPending
        }
        onConfirm={confirmarDesactivar}
        onClose={() => {

            setConfirmDialogOpen(false);

            setBeneficiarioSeleccionado(
                null,
            );

        }}
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