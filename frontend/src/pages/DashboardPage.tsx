import {
  Box,
  Button,
  Card,
  CardContent,
  CircularProgress,
  Grid,
  Stack,
  Typography,
} from "@mui/material";

import Inventory2Icon from "@mui/icons-material/Inventory2";
import PeopleIcon from "@mui/icons-material/People";
import HandshakeIcon from "@mui/icons-material/Handshake";
import BuildIcon from "@mui/icons-material/Build";

import { useNavigate } from "react-router-dom";

import { useAuth } from "../contexts/AuthContext";

import { useDashboard } from "@/modules/dashboard/hooks/useDashboard";

export default function DashboardPage() {
  const navigate = useNavigate();

  const { logout } = useAuth();

  const {
    totalImplementos,
    totalBeneficiarios,
    prestamosActivos,
    loading,
  } = useDashboard();

  function handleLogout() {
    logout();

    navigate("/", {
      replace: true,
    });
  }

  return (
    <Box sx={{ p: 4 }}>
      <Typography
        variant="h4"
        fontWeight="bold"
        gutterBottom
      >
        SIGIO
      </Typography>

      <Typography
        color="text.secondary"
        sx={{ mb: 4 }}
      >
        Sistema Integral de Gestión de Implementos
        Ortopédicos
      </Typography>

      {loading ? (
        <Stack
          alignItems="center"
          py={8}
        >
          <CircularProgress />
        </Stack>
      ) : (
        <>
          <Grid
            container
            spacing={3}
            sx={{ mb: 4 }}
          >
            <Grid size={{ xs: 12, sm: 6, md: 3 }}>
              <Card elevation={3}>
                <CardContent>
                  <Stack
                    direction="row"
                    spacing={2}
                    alignItems="center"
                  >
                    <Inventory2Icon
                      color="primary"
                      fontSize="large"
                    />

                    <Box>
                      <Typography
                        variant="body2"
                        color="text.secondary"
                      >
                        Implementos
                      </Typography>

                      <Typography variant="h4">
                        {totalImplementos}
                      </Typography>
                    </Box>
                  </Stack>
                </CardContent>
              </Card>
            </Grid>

            <Grid size={{ xs: 12, sm: 6, md: 3 }}>
              <Card elevation={3}>
                <CardContent>
                  <Stack
                    direction="row"
                    spacing={2}
                    alignItems="center"
                  >
                    <PeopleIcon
                      color="primary"
                      fontSize="large"
                    />

                    <Box>
                      <Typography
                        variant="body2"
                        color="text.secondary"
                      >
                        Beneficiarios
                      </Typography>

                      <Typography variant="h4">
                        {totalBeneficiarios}
                      </Typography>
                    </Box>
                  </Stack>
                </CardContent>
              </Card>
            </Grid>

            <Grid size={{ xs: 12, sm: 6, md: 3 }}>
              <Card elevation={3}>
                <CardContent>
                  <Stack
                    direction="row"
                    spacing={2}
                    alignItems="center"
                  >
                    <HandshakeIcon
                      color="primary"
                      fontSize="large"
                    />

                    <Box>
                      <Typography
                        variant="body2"
                        color="text.secondary"
                      >
                        Préstamos activos
                      </Typography>

                      <Typography variant="h4">
                        {prestamosActivos}
                      </Typography>
                    </Box>
                  </Stack>
                </CardContent>
              </Card>
            </Grid>

            <Grid size={{ xs: 12, sm: 6, md: 3 }}>
              <Card elevation={3}>
                <CardContent>
                  <Stack
                    direction="row"
                    spacing={2}
                    alignItems="center"
                  >
                    <BuildIcon
                      color="disabled"
                      fontSize="large"
                    />

                    <Box>
                      <Typography
                        variant="body2"
                        color="text.secondary"
                      >
                        Mantenimientos
                      </Typography>

                      <Typography variant="h4">
                        —
                      </Typography>

                      <Typography
                        variant="caption"
                        color="text.secondary"
                      >
                        Próximamente
                      </Typography>
                    </Box>
                  </Stack>
                </CardContent>
              </Card>
            </Grid>
          </Grid>

          <Typography
            variant="h5"
            gutterBottom
          >
            Accesos rápidos
          </Typography>

          <Grid
            container
            spacing={3}
          >
            <Grid size={{ xs: 12, md: 4 }}>
              <Card>
                <CardContent>
                  <Typography
                    variant="h6"
                    gutterBottom
                  >
                    📦 Implementos
                  </Typography>

                  <Typography
                    color="text.secondary"
                    sx={{ mb: 2 }}
                  >
                    Administración del inventario de
                    implementos ortopédicos.
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
                </CardContent>
              </Card>
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Card>
                <CardContent>
                  <Typography
                    variant="h6"
                    gutterBottom
                  >
                    👥 Beneficiarios
                  </Typography>

                  <Typography
                    color="text.secondary"
                    sx={{ mb: 2 }}
                  >
                    Gestión de beneficiarios del
                    sistema.
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
                </CardContent>
              </Card>
            </Grid>

            <Grid size={{ xs: 12, md: 4 }}>
              <Card>
                <CardContent>
                  <Typography
                    variant="h6"
                    gutterBottom
                  >
                    🤝 Préstamos
                  </Typography>

                  <Typography
                    color="text.secondary"
                    sx={{ mb: 2 }}
                  >
                    Administración de préstamos y
                    devoluciones.
                  </Typography>

                  <Button
                    fullWidth
                    variant="contained"
                    onClick={() =>
                      navigate("/prestamos")
                    }
                  >
                    Ingresar
                  </Button>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </>
      )}

      <Button
        sx={{ mt: 5 }}
        color="error"
        variant="outlined"
        onClick={handleLogout}
      >
        Cerrar sesión
      </Button>
    </Box>
  );
}