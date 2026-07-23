import { useMutation, useQueryClient } from "@tanstack/react-query";

import prestamoService from "../services/prestamoService";

export function useCrearPrestamo() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: prestamoService.crear,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["prestamos"],
      });
    },
  });
}