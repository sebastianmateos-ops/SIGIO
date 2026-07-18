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

import TableActions from "@/shared/components/TableActions";

import type { Beneficiario } from "../types/beneficiario";

interface Props {
  rows: Beneficiario[];
  loading: boolean;
  error: boolean;

  onEditar?: (
    beneficiario: Beneficiario,
  ) => void;

  onVer?: (
    beneficiario: Beneficiario,
  ) => void;

  onDesactivar?: (
    beneficiario: Beneficiario,
  ) => void;
}

function colorActivo(activo: boolean) {
  return activo ? "success" : "error";
}

export default function BeneficiariosTable({
  rows,
  loading,
  error,
  onEditar,
  onVer,
  onDesactivar,
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

  const columns: GridColDef<Beneficiario>[] = [
    {
      field: "codigo",
      headerName: "Código",
      width: 120,
    },
    {
      field: "numero_documento",
      headerName: "Documento",
      width: 140,
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
      width: 120,
    },
    {
      field: "celular",
      headerName: "Celular",
      width: 120,
    },
    {
      field: "ciudad",
      headerName: "Ciudad",
      width: 140,
    },
    {
      field: "activo",
      headerName: "Estado",
      width: 110,

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
    {
      field: "acciones",
      headerName: "Acciones",
      width: 140,
      sortable: false,
      filterable: false,
      disableColumnMenu: true,

      renderCell: (params) => (
        <TableActions
          onView={() =>
            onVer?.(params.row)
          }
          onEdit={() =>
            onEditar?.(params.row)
          }
          onDeactivate={() =>
            onDesactivar?.(params.row)
          }
        />
      ),
    },
  ];

  return (
    <Paper sx={{ height: 560 }}>
      <DataGrid
        rows={rows}
        columns={columns}
        getRowId={(row) => row.id}
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