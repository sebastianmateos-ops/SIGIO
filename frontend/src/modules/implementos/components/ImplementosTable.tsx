import {
  Alert,
  Chip,
  CircularProgress,
  Paper,
} from "@mui/material";

import {
  DataGrid,
  type GridColDef,
} from "@mui/x-data-grid";

import type { Implemento } from "../types/implemento";

interface Props {
  rows: Implemento[];
  loading: boolean;
  error: boolean;
}

function colorEstado(estado: string) {
  switch (estado) {
    case "Disponible":
      return "success";

    case "Prestado":
      return "warning";

    case "Mantenimiento":
      return "info";

    case "Fuera de servicio":
      return "error";

    default:
      return "default";
  }
}

const columns: GridColDef[] = [
  {
    field: "codigo",
    headerName: "Código",
    width: 150,
  },
  {
    field: "categoria",
    headerName: "Categoría",
    flex: 1,
  },
  {
    field: "marca",
    headerName: "Marca",
    width: 140,
  },
  {
    field: "modelo",
    headerName: "Modelo",
    width: 160,
  },
  {
    field: "estado",
    headerName: "Estado",
    width: 180,

    renderCell: (params) => (
      <Chip
        label={params.value}
        color={colorEstado(params.value)}
        size="small"
      />
    ),
  },
  {
    field: "ubicacion",
    headerName: "Ubicación",
    flex: 1,
  },
];

export default function ImplementosTable({
  rows,
  loading,
  error,
}: Props) {
  if (loading) {
    return <CircularProgress />;
  }

  if (error) {
    return (
      <Alert severity="error">
        No fue posible cargar los implementos.
      </Alert>
    );
  }

  return (
    <Paper sx={{ height: 560 }}>
      <DataGrid
        rows={rows}
        columns={columns}
        disableRowSelectionOnClick
        pageSizeOptions={[10, 20, 50]}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 10,
            },
          },
        }}
      />
    </Paper>
  );
}