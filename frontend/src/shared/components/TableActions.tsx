import {
  Box,
  IconButton,
  Tooltip,
} from "@mui/material";

import VisibilityIcon from "@mui/icons-material/Visibility";
import EditIcon from "@mui/icons-material/Edit";
import BlockIcon from "@mui/icons-material/Block";

interface TableActionsProps {
  onView?: () => void;
  onEdit?: () => void;
  onDeactivate?: () => void;
}

export default function TableActions({
  onView,
  onEdit,
  onDeactivate,
}: TableActionsProps) {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        gap: 0.5,
        width: "100%",
        height: "100%",
      }}
    >
      <Tooltip title="Ver">
        <IconButton
          size="small"
          onClick={onView}
        >
          <VisibilityIcon fontSize="small" />
        </IconButton>
      </Tooltip>

      <Tooltip title="Editar">
        <IconButton
          size="small"
          color="primary"
          onClick={onEdit}
        >
          <EditIcon fontSize="small" />
        </IconButton>
      </Tooltip>

      <Tooltip title="Desactivar">
        <IconButton
          size="small"
          color="error"
          onClick={onDeactivate}
        >
          <BlockIcon fontSize="small" />
        </IconButton>
      </Tooltip>
    </Box>
  );
}