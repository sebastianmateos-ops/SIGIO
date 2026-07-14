import { ReactNode } from "react";

import {
  Box,
  Button,
  Typography,
} from "@mui/material";

import ArrowBackIcon from "@mui/icons-material/ArrowBack";

import { useNavigate } from "react-router-dom";

interface PageHeaderProps {
  title: string;
  backTo?: string;
  action?: ReactNode;
}

export default function PageHeader({
  title,
  backTo,
  action,
}: PageHeaderProps) {
  const navigate = useNavigate();

  return (
    <Box
      sx={{
        mb: 4,
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      <Box
        sx={{
          display: "flex",
          alignItems: "center",
          gap: 2,
        }}
      >
        {backTo && (
          <Button
            variant="outlined"
            startIcon={<ArrowBackIcon />}
            onClick={() => navigate(backTo)}
          >
            Volver
          </Button>
        )}

        <Typography variant="h4">
          {title}
        </Typography>
      </Box>

      {action}
    </Box>
  );
}