import { useState } from "react";

import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Stack,
  TextField,
} from "@mui/material";

interface Props {
  open: boolean;
  loading?: boolean;
  onClose: () => void;
  onConfirm: (observaciones: string) => void;
}

export default function DevolverPrestamoDialog({
  open,
  loading = false,
  onClose,
  onConfirm,
}: Props) {
  const [observaciones, setObservaciones] = useState("");

  const handleCerrar = () => {
    setObservaciones("");
    onClose();
  };

  const handleConfirmar = () => {
    onConfirm(observaciones);
    setObservaciones("");
  };

  return (
    <Dialog
      open={open}
      onClose={handleCerrar}
      fullWidth
      maxWidth="sm"
    >
      <DialogTitle>
        Registrar devolución
      </DialogTitle>

      <DialogContent>
        <Stack mt={1}>
          <TextField
            label="Observaciones"
            multiline
            minRows={4}
            value={observaciones}
            onChange={(e) => setObservaciones(e.target.value)}
            fullWidth
          />
        </Stack>
      </DialogContent>

      <DialogActions>
        <Button
          onClick={handleCerrar}
          disabled={loading}
        >
          Cancelar
        </Button>

        <Button
          variant="contained"
          onClick={handleConfirmar}
          disabled={loading}
        >
          Registrar devolución
        </Button>
      </DialogActions>
    </Dialog>
  );
}