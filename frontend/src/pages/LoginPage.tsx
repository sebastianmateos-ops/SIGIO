import {
  Box,
  Card,
  CardContent,
  Container,
  Stack,
  Typography,
} from "@mui/material";

import LoginForm from "../components/forms/LoginForm";

export default function LoginPage() {
  return (
    <Box
      sx={{
        minHeight: "100vh",
        backgroundColor: "background.default",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        p: 3,
      }}
    >
      <Container maxWidth="sm">
        <Card
          elevation={6}
          sx={{
            borderRadius: 3,
          }}
        >
          <CardContent
            sx={{
              p: 5,
            }}
          >
            <Stack
              spacing={3}
              sx={{
                alignItems: "center",
              }}
            >
              {/* Espacio reservado para el logo institucional */}

              <Box
                sx={{
                  width: 130,
                  height: 130,
                  border: "2px dashed",
                  borderColor: "primary.main",
                  borderRadius: 2,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  color: "primary.main",
                  fontWeight: 700,
                  fontSize: 18,
                }}
              >
                LOGO
              </Box>

              <Typography
                variant="h4"
                color="primary"
                sx={{
                  fontWeight: 700,
                }}
                align="center"
              >
                SIGIO
              </Typography>

              <Typography
                variant="subtitle1"
                align="center"
                color="text.secondary"
              >
                Sistema de Gestión
                <br />
                de Implementos Ortopédicos
              </Typography>

              <LoginForm />

              <Box
                sx={{
                  textAlign: "center",
                }}
              >
                <Typography
                  variant="body2"
                  color="text.secondary"
                >
                  Club de Leones
                </Typography>

                <Typography
                  variant="body2"
                  color="text.secondary"
                >
                  San José de Mayo
                </Typography>

                <Typography
                  variant="caption"
                  color="text.secondary"
                  sx={{
                    display: "block",
                    mt: 2,
                  }}
                >
                  SIGIO v1.0
                </Typography>
              </Box>

            </Stack>
          </CardContent>
        </Card>
      </Container>
    </Box>
  );
}