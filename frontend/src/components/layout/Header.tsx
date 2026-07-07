import {
  AppBar,
  Box,
  Toolbar,
  Typography,
} from "@mui/material";

export default function Header() {
  return (
    <AppBar
      position="sticky"
      elevation={1}
    >
      <Toolbar>

        <Typography
          variant="h6"
          component="div"
          sx={{
            fontWeight: 700,
            letterSpacing: 1,
          }}
        >
          SIGIO
        </Typography>

        <Box sx={{ flexGrow: 1 }} />

        <Typography
          variant="body2"
          sx={{
            opacity: 0.90,
          }}
        >
          Sistema de Gestión de Implementos Ortopédicos
        </Typography>

      </Toolbar>
    </AppBar>
  );
}