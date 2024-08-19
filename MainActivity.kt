interface AuthApi {
    @POST("/register")
    suspend fun register(@Body user: User): Response<Void>

    @POST("/login")
    suspend fun login(@Body user: User): Response<LoginResponse>
}
