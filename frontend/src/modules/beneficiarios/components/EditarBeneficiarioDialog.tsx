import { useEffect } from "react";

import { zodResolver } from "@hookform/resolvers/zod";

import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
} from "@mui/material";

import {
  FormProvider,
  useForm,
} from "react-hook-form";

import BeneficiarioForm from "./BeneficiarioForm";

import type { Beneficiario } from "../types/beneficiario";

import {
  beneficiarioSchema,
  type BeneficiarioFormData,
} from "../schemas/beneficiarioSchema";

interface Props {
  open: boolean;

  loading: boolean;

  beneficiario: Beneficiario | null;

  onClose: () => void;

  onGuardar: (
    datos: BeneficiarioFormData,
  ) => Promise<void>;
}

export default function EditarBeneficiarioDialog({
  open,
  loading,
  beneficiario,
  onClose,
  onGuardar,
}: Props) {
  const methods =
    useForm<BeneficiarioFormData>({
      resolver: zodResolver(
        beneficiarioSchema,
      ),

      defaultValues: {
        tipo_documento: "CI",
        numero_documento: "",
        nombre: "",
        apellido: "",
        fecha_nacimiento: null,
        telefono: "",
        celular: "",
        email: "",
        direccion: "",
        ciudad: "",
        departamento: "",
        observaciones: "",
      },
    });

  useEffect(() => {
    if (!beneficiario) {
      return;
    }

    methods.reset({
      tipo_documento:
        beneficiario.tipo_documento,

      numero_documento:
        beneficiario.numero_documento,

      nombre:
        beneficiario.nombre,

      apellido:
        beneficiario.apellido,

      fecha_nacimiento:
        beneficiario.fecha_nacimiento,

      telefono:
        beneficiario.telefono ?? "",

      celular:
        beneficiario.celular ?? "",

      email:
        beneficiario.email ?? "",

      direccion:
        beneficiario.direccion ?? "",

      ciudad:
        beneficiario.ciudad ?? "",

      departamento:
        beneficiario.departamento ?? "",

      observaciones:
        beneficiario.observaciones ?? "",
    });

  }, [beneficiario, methods]);

  async function submit(
    datos: BeneficiarioFormData,
  ) {
    await onGuardar(datos);
  }

  return (
    <Dialog
      open={open}
      onClose={onClose}
      maxWidth="md"
      fullWidth
    >
      <DialogTitle>
        Editar Beneficiario
      </DialogTitle>

      <FormProvider {...methods}>
        <form
          onSubmit={methods.handleSubmit(
            submit,
          )}
        >
          <DialogContent>
            <BeneficiarioForm />
          </DialogContent>

          <DialogActions>
            <Button
              onClick={onClose}
            >
              Cancelar
            </Button>

            <Button
              type="submit"
              variant="contained"
              disabled={loading}
            >
              {loading
                ? "Guardando..."
                : "Guardar cambios"}
            </Button>
          </DialogActions>
        </form>
      </FormProvider>
    </Dialog>
  );
}