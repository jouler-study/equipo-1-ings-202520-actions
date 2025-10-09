
# 🔐 Plaze Login API

## 🚀 Setup

1️⃣ Go to the `server` folder in the project.

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Create a `.env` file **inside the same folder (`server/`)** with the following structure:

```
DATABASE_URL=
EMAIL_USER=
EMAIL_PASS=
SECRET_KEY=
ALGORITHM =
ACCESS_TOKEN_EXPIRE_MINUTES =
```

Replace the values with the credentials shared by the team.

4️⃣ Run the API:

```bash
uvicorn main:app --reload
```

The API documentation is available at:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔑 Login

### 🔹 `/auth/login`

**POST**

**Body:**

```json
{
  "correo": "user@example.com",
  "contrasena": "1234"
}
```

**Response:**

```json
{
  "message": "Inicio de sesión exitoso",
  "user": "user@example.com",
  "role": "usuario",
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

📌 The `access_token` is returned in the response after login — this is the token you will use to log out.

**Account Lock Test:**

* To test the account block feature, enter the **wrong password 3 times**.
* A recovery email will be sent to the user.
* You can register using your own email or with already existing emails for testing.

---

## 🚪 Logout

### 🔹 `/auth/logout`

**POST**

**Header:**

```
Bearer <access_token>
```

Add it in the **lock icon (Authorize)** in Swagger, then click **Close**. After that, click in Try it out and execute. The response should look like the example below:

**Response:**

```json
{ "message": "Sesión cerrada correctamente" }
```

---

## 🔐 Password Recovery

### 🔹 `/password/recover`

**POST**

**Body:**

```json
{
  "correo": "user@example.com"
}
```

**Description:** The argument is the user's email (`correo`).

**Response:**

```json
{ "message": "Correo de recuperación de contraseña enviado exitosamente" }
```

---

### 🔹 `/password/reset/{token}`

**POST**

**Body:**

```json
{
  "nueva_contrasena": "newpassword123"
}
```

**Response:**

```json
{ "message": "Contraseña restablecida exitosamente" }
```
