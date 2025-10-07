

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
  "message": "Login successful",
  "user": "user@example.com",
  "role": "user",
  "access_token": "eyJhbGciOi...",
  "token_type": "bearer"
}
```

📌 The `access_token` is returned in the response after login — this is the token you will use to log out.

---

## 🚪 Logout

### 🔹 `/auth/logout`

**POST**

**Header:**

```
Bearer <access_token>
```

Add it in the **lock icon (Authorize)** in Swagger, then click **Close**.

**Response:**

```json
{ "message": "Logged out successfully" }
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
{ "message": "Password recovery email sent successfully" }
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
{ "message": "Password reset successfully" }
```

---
