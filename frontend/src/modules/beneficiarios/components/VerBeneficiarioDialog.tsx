import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Divider,
  Grid,
  Typography,
} from "@mui/material";

import type { Beneficiario } from "../types/beneficiario";

interface Props {
  open: boolean;
  beneficiario: Beneficiario | null;
  onClose: () => void;
}

function Item({
  label,
  value,
}: {
  label: string;
  value?: string | null;
}) {
  return (
    <Grid size={{ xs: 12, md: 6 }}>
      <Typography
        variant="caption"
        color="text.secondary"
      >
        {label}
      </Typography>

      <Typography>
        {value || "-"}
      </Typography>
    </Grid>
  );
}

export default function VerBeneficiarioDialog({
  open,
  beneficiario,
  onClose,
}: Props) {
  if (!beneficiario) {
    return null;
  }

  return (
    <Dialog
      open={open}
      onClose={onClose}
      fullWidth
      maxWidth="md"
    >
      <DialogTitle>
        Beneficiario
      </DialogTitle>

      <DialogContent dividers>
        <Grid
          container
          spacing={2}
        >
          <Item
            label="Código"
            value={beneficiario.codigo}
          />

          <Item
            label="Documento"
            value={`${beneficiario.tipo_documento} ${beneficiario.numero_documento}`}
          />

          <Item
            label="Nombre"
            value={beneficiario.nombre}
          />

          <Item
            label="Apellido"
            value={beneficiario.apellido}
          />

          <Item
            label="Fecha de nacimiento"
            value={beneficiario.fecha_nacimiento}
          />

          <Item
            label="Teléfono"
            value={beneficiario.telefono}
          />

          <Item
            label="Celular"
            value={beneficiario.celular}
          />

          <Item
            label="Correo electrónico"
            value={beneficiario.email}
          />

          <Item
            label="Ciudad"
            value={beneficiario.ciudad}
          />

          <Item
            label="Departamento"
            value={beneficiario.departamento}
          />

          <Grid size={{ xs: 12 }}>
            <Divider sx={{ my: 1 }} />
          </Grid>

          <Grid size={{ xs: 12 }}>
            <Typography
              variant="caption"
              color="text.secondary"
            >
              Dirección
            </Typography>

            <Typography>
              {beneficiario.direccion || "-"}
            </Typography>
          </Grid>

          <Grid size={{ xs: 12 }}>
            <Typography
              variant="caption"
              color="text.secondary"
            >
              Observaciones
            </Typography>

            <Typography>
              {beneficiario.observaciones || "-"}
            </Typography>
          </Grid>
        </Grid>
      </DialogContent>

      <DialogActions>
        <Button onClick={onClose}>
          Cerrar
        </Button>
      </DialogActions>
    </Dialog>
  );
}