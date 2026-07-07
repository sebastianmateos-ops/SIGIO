import {
  Box,
  Card,
  CardContent,
  Divider,
  Stack,
  Typography,
} from "@mui/material";

import MainLayout from "../layouts/MainLayout";

export default function HomePage() {
  return (
    <MainLayout>
      <Card>
        <CardContent>
          <Stack spacing={3}>

            <Typography
              variant="h4"
              color="primary"
              fontWeight="bold"
            >
              SIGIO
            </Typography>

            <Typography variant="h6">
              Sistema de Gestión de Implementos Ortopédicos
            </Typography>

            <Divider />

            <Typography color="text.secondary">
              Club de Leones San José de Mayo
            </Typography>

            <Box pt={2}>
              <Typography variant="body1">
                Bienvenido al Sistema de Gestión de Implementos
                Ortopédicos.
              </Typography>

              <Typography
                variant="body2"
                color="text.secondary"
                sx={{ mt: 2 }}
              >
                El frontend se encuentra correctamente inicializado
                y preparado para comenzar el desarrollo de los
                módulos funcionales.
              </Typography>
            </Box>

          </Stack>
        </CardContent>
      </Card>
    </MainLayout>
  );
}