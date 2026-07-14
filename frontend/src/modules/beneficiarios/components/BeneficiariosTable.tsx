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

import type { Beneficiario } from "../types/beneficiario";

interface Props {
  rows: Beneficiario[];
  loading: boolean;
  error: boolean;
}

function colorActivo(
  activo: boolean,
) {
  return activo
    ? "success"
    : "error";
}

const columns: GridColDef[] = [
  {
    field: "codigo",
    headerName: "Código",
    width: 130,
  },
  {
    field: "numero_documento",
    headerName: "Documento",
    width: 130,
  },
  {
    field: "nombreCompleto",
    headerName: "Beneficiario",
    flex: 1,
    valueGetter: (_, row) =>
      `${row.apellido}, ${row.nombre}`,
  },
  {
    field: "telefono",
    headerName: "Teléfono",
    width: 140,
  },
  {
    field: "celular",
    headerName: "Celular",
    width: 140,
  },
  {
    field: "ciudad",
    headerName: "Ciudad",
    width: 160,
  },
  {
    field: "activo",
    headerName: "Estado",
    width: 130,

    renderCell: (params) => (
      <Chip
        label={
          params.value
            ? "Activo"
            : "Inactivo"
        }
        color={colorActivo(params.value)}
        size="small"
      />
    ),
  },
];

export default function BeneficiariosTable({
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
        No fue posible cargar los beneficiarios.
      </Alert>
    );
  }

  return (
    <Paper
      sx={{
        height: 560,
      }}
    >
      <DataGrid
        rows={rows}
        columns={columns}
        disableRowSelectionOnClick
        pageSizeOptions={[
          10,
          20,
          50,
        ]}
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