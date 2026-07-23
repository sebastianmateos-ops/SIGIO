import { useQuery } from "@tanstack/react-query";

import prestamoService from "../services/prestamoService";

export function usePrestamos() {
  return useQuery({
    queryKey: ["prestamos"],

    queryFn: () =>
      prestamoService.listar(),
  });
}