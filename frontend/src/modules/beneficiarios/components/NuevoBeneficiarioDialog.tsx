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

import {
  beneficiarioSchema,
  type BeneficiarioFormData,
} from "../schemas/beneficiarioSchema";

interface Props {
  open: boolean;

  loading: boolean;

  onClose: () => void;

  onGuardar: (
    datos: BeneficiarioFormData,
  ) => Promise<void>;
}

export default function NuevoBeneficiarioDialog({
  open,
  loading,
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

  async function submit(
    datos: BeneficiarioFormData,
  ) {
    await onGuardar(datos);

    methods.reset();
  }

  return (
    <Dialog
      open={open}
      onClose={onClose}
      maxWidth="md"
      fullWidth
    >
      <DialogTitle>
        Nuevo Beneficiario
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
                : "Guardar"}
            </Button>
          </DialogActions>
        </form>
      </FormProvider>
    </Dialog>
  );
}