import {
  Alert,
  Snackbar,
} from "@mui/material";

interface Props {
  open: boolean;
  message: string;
  severity: "success" | "error";
  onClose: () => void;
}

export default function SnackbarMessage({
  open,
  message,
  severity,
  onClose,
}: Props) {
  return (
    <Snackbar
      open={open}
      autoHideDuration={4000}
      onClose={onClose}
      anchorOrigin={{
        vertical: "bottom",
        horizontal: "right",
      }}
    >
      <Alert
        severity={severity}
        onClose={onClose}
        variant="filled"
        sx={{ width: "100%" }}
      >
        {message}
      </Alert>
    </Snackbar>
  );
}