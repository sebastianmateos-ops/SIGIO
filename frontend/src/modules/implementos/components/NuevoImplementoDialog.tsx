import {
  Dialog,
  DialogContent,
  DialogTitle,
} from "@mui/material";

import type { ImplementoFormData } from "../schemas/implementoSchema";
import ImplementoForm from "./ImplementoForm";

import type { Categoria } from "@/modules/catalogos/categorias/types/categoria";


interface Props {
  open: boolean;
  onClose: () => void;

  categorias: Categoria[];

  onGuardar: (
    datos: ImplementoFormData,
  ) => void;

  loading?: boolean;
}

export default function NuevoImplementoDialog({
  open,
  onClose,
  categorias,
  onGuardar,
  loading = false,
}: Props) {
  return (
    <Dialog
      open={open}
      onClose={onClose}
      fullWidth
      maxWidth="md"
    >
      <DialogTitle>
        Nuevo Implemento
      </DialogTitle>

      <DialogContent sx={{ pt: 2 }}>
        <ImplementoForm
          categorias={categorias}
          onSubmit={onGuardar}
          loading={loading}
        />
      </DialogContent>
    </Dialog>
  );
}