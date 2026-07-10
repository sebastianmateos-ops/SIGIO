import { useMutation, useQueryClient } from "@tanstack/react-query";

import implementoService from "../services/implementoService";

export function useCrearImplemento() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: implementoService.crear,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["implementos"],
      });
    },
  });
}