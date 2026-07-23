import { useMutation, useQueryClient } from "@tanstack/react-query";

import prestamoService, {
  type PrestamoUpdate,
} from "../services/prestamoService";

interface DevolverPrestamoParams {
  id: number;
  datos: PrestamoUpdate;
}

export function useDevolverPrestamo() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, datos }: DevolverPrestamoParams) =>
      prestamoService.devolver(id, datos),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["prestamos"],
      });

      queryClient.invalidateQueries({
        queryKey: ["implementos"],
      });
    },
  });
}