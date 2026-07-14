import {
  Box,
  Button,
  Grid,
  Paper,
  Typography,
} from "@mui/material";

import { useNavigate } from "react-router-dom";

import { useAuth } from "../contexts/AuthContext";

export default function DashboardPage() {
  const navigate = useNavigate();

  const { logout } = useAuth();

  function handleLogout() {
    logout();
    navigate("/", {
      replace: true,
    });
  }

  return (
    <Box
      sx={{
        p: 4,
      }}
    >
      <Typography
        variant="h4"
        gutterBottom
      >
        SIGIO
      </Typography>

      <Typography
        sx={{
          mb: 4,
        }}
      >
        Sistema Integral de Gestión de Implementos Ortopédicos
      </Typography>

      <Grid
        container
        spacing={3}
      >
        <Grid size={{ xs: 12, md: 4 }}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6">
              Implementos
            </Typography>

            <Typography sx={{ my: 2 }}>
              Administración del inventario.
            </Typography>

            <Button
              fullWidth
              variant="contained"
              onClick={() =>
                navigate("/implementos")
              }
            >
              Ingresar
            </Button>
          </Paper>
        </Grid>

        <Grid size={{ xs: 12, md: 4 }}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6">
              Beneficiarios
            </Typography>

            <Typography sx={{ my: 2 }}>
              Administración de beneficiarios.
            </Typography>

            <Button
              fullWidth
              variant="contained"
              onClick={() =>
                navigate("/beneficiarios")
              }
            >
              Ingresar
            </Button>
          </Paper>
        </Grid>

        <Grid size={{ xs: 12, md: 4 }}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6">
              Préstamos
            </Typography>

            <Typography sx={{ my: 2 }}>
              Próximamente
            </Typography>

            <Button
              fullWidth
              disabled
            >
              Disponible próximamente
            </Button>
          </Paper>
        </Grid>
      </Grid>

      <Button
        sx={{
          mt: 5,
        }}
        color="error"
        variant="outlined"
        onClick={handleLogout}
      >
        Cerrar sesión
      </Button>
    </Box>
  );
}