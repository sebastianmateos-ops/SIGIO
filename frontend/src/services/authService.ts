import api from "../api/axios";

export interface LoginRequest {
  usuario: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

class AuthService {
  async login(
    credentials: LoginRequest,
  ): Promise<LoginResponse> {
    const formData = new URLSearchParams();

    formData.append("username", credentials.usuario);
    formData.append("password", credentials.password);

    const response = await api.post<LoginResponse>(
      "/auth/login",
      formData,
      {
        headers: {
          "Content-Type":
            "application/x-www-form-urlencoded",
        },
      },
    );

    return response.data;
  }
}

export default new AuthService();