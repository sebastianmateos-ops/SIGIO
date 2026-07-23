import {
  Dialog,
  DialogContent,
  DialogTitle,
} from "@mui/material";

import PrestamoForm from "./PrestamoForm";

import type { Implemento } from "@/modules/implementos/types/implemento";
import type { Beneficiario } from "@/modules/beneficiarios/types/beneficiario";

import type { PrestamoFormData } from "../schemas/prestamoSchema";

interface Props {
  open: boolean;
  onClose: () => void;
  implementos: Implemento[];
  beneficiarios: Beneficiario[];
  onGuardar: (data: PrestamoFormData) => void;
  loading?: boolean;
}

export default function NuevoPrestamoDialog({
  open,
  onClose,
  implementos,
  beneficiarios,
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
      <DialogTitle>Nuevo préstamo</DialogTitle>

      <DialogContent sx={{ pt: 2 }}>
        <PrestamoForm
          implementos={implementos}
          beneficiarios={beneficiarios}
          onSubmit={onGuardar}
          loading={loading}
        />
      </DialogContent>
    </Dialog>
  );
}