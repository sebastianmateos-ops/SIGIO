import { useQuery } from "@tanstack/react-query";

import beneficiarioService from "../services/beneficiarioService";

export function useBeneficiarios() {
  return useQuery({
    queryKey: ["beneficiarios"],

    queryFn: () =>
      beneficiarioService.listar(),
  });
}