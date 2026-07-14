import { useMutation, useQueryClient } from "@tanstack/react-query";

import beneficiarioService from "../services/beneficiarioService";

export function useEliminarBeneficiario() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: beneficiarioService.eliminar,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["beneficiarios"],
      });
    },
  });
}