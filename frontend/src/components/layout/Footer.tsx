import {
  Box,
  Divider,
  Typography,
} from "@mui/material";

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <>
      <Divider />

      <Box
        component="footer"
        sx={{
          py: 2,
          px: 3,
          mt: "auto",
          bgcolor: "background.paper",
          textAlign: "center",
        }}
      >
        <Typography
          variant="body2"
          color="text.secondary"
        >
          SIGIO · Sistema de Gestión de Implementos Ortopédicos
        </Typography>

        <Typography
          variant="caption"
          color="text.secondary"
          display="block"
          sx={{ mt: 0.5 }}
        >
          Club de Leones San José de Mayo · © {currentYear}
        </Typography>
      </Box>
    </>
  );
}