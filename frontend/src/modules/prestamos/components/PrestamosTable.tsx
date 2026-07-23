import {
  Alert,
  Button,
  Chip,
  CircularProgress,
  Paper,
} from "@mui/material";

import {
  DataGrid,
  type GridColDef,
} from "@mui/x-data-grid";

import type { Prestamo } from "../services/prestamoService";

interface Props {
  rows: Prestamo[];
  loading: boolean;
  error: boolean;
  onDevolver: (prestamo: Prestamo) => void;
}

const columns = (
  onDevolver: (prestamo: Prestamo) => void,
): GridColDef[] => [
  {
    field: "codigo",
    headerName: "Código",
    width: 140,
    valueGetter: (_, row) => row.implemento.codigo,
  },
  {
    field: "implemento",
    headerName: "Implemento",
    flex: 1,
    valueGetter: (_, row) =>
      `${row.implemento.marca ?? ""} ${row.implemento.modelo ?? ""}`.trim(),
  },
  {
    field: "beneficiario",
    headerName: "Beneficiario",
    flex: 1,
    valueGetter: (_, row) =>
      `${row.beneficiario.nombre} ${row.beneficiario.apellido}`,
  },
  {
    field: "fecha_prestamo",
    headerName: "Préstamo",
    width: 180,
    valueFormatter: (value: string) =>
      new Date(value).toLocaleString(),
  },
  {
    field: "estado",
    headerName: "Estado",
    width: 140,
    renderCell: (params) => {
      const abierto = !params.row.fecha_devolucion;

      return (
        <Chip
          label={abierto ? "Vigente" : "Finalizado"}
          color={abierto ? "warning" : "success"}
          size="small"
        />
      );
    },
  },
  {
    field: "acciones",
    headerName: "Acciones",
    width: 150,
    sortable: false,
    renderCell: (params) =>
      !params.row.fecha_devolucion ? (
        <Button
          size="small"
          variant="contained"
          onClick={() => onDevolver(params.row)}
        >
          Devolver
        </Button>
      ) : null,
  },
];

export default function PrestamosTable({
  rows,
  loading,
  error,
  onDevolver,
}: Props) {
  if (loading) {
    return <CircularProgress />;
  }

  if (error) {
    return (
      <Alert severity="error">
        No fue posible cargar los préstamos.
      </Alert>
    );
  }

  return (
    <Paper sx={{ height: 560 }}>
      <DataGrid
        rows={rows}
        columns={columns(onDevolver)}
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