import {
  Box,
  Button,
  Stack,
  Typography,
} from "@mui/material";

import { Link } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

export default function NotFoundPage() {
  return (
    <MainLayout>
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          minHeight: "60vh",
        }}
      >
        <Stack
          spacing={3}
          sx={{
            alignItems: "center",
          }}
        >
          <Typography
            variant="h1"
            color="primary"
            sx={{
              fontWeight: "bold",
            }}
          >
            404
          </Typography>

          <Typography variant="h5">
            Página no encontrada
          </Typography>

          <Typography
            color="text.secondary"
            align="center"
          >
            La página solicitada no existe
            o fue movida.
          </Typography>

          <Button
            component={Link}
            to="/"
            color="primary"
          >
            Volver al inicio
          </Button>
        </Stack>
      </Box>
    </MainLayout>
  );
}