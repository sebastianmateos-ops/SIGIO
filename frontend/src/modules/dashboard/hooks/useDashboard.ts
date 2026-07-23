import { useMemo } from "react";

import { useImplementos } from "@/modules/implementos/hooks/useImplementos";
import { useBeneficiarios } from "@/modules/beneficiarios/hooks/useBeneficiarios";
import { usePrestamos } from "@/modules/prestamos/hooks/usePrestamos";

export function useDashboard() {
  const {
    data: implementos = [],
    isLoading: loadingImplementos,
  } = useImplementos();

  const {
    data: beneficiarios = [],
    isLoading: loadingBeneficiarios,
  } = useBeneficiarios();

  const {
    data: prestamos = [],
    isLoading: loadingPrestamos,
  } = usePrestamos();

  const indicadores = useMemo(() => {
    const prestamosActivos = prestamos.filter(
      (prestamo) => prestamo.fecha_devolucion === null,
    ).length;

    return {
      totalImplementos: implementos.length,
      totalBeneficiarios: beneficiarios.length,
      prestamosActivos,
    };
  }, [
    implementos,
    beneficiarios,
    prestamos,
  ]);

  return {
    ...indicadores,

    loading:
      loadingImplementos ||
      loadingBeneficiarios ||
      loadingPrestamos,
  };
}