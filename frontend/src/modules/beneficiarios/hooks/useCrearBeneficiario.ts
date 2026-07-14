import { useMutation, useQueryClient } from "@tanstack/react-query";

import beneficiarioService from "../services/beneficiarioService";

export function useCrearBeneficiario() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: beneficiarioService.crear,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["beneficiarios"],
      });
    },
  });
}