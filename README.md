<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin-bottom: 8px;
        }

        input {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        select {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #4caf50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>

<form>
    <label for="firstName">First Name:</label>
    <input type="text" id="firstName" placeholder="Enter your first name" required>

    <label for="lastName">Last Name:</label>
    <input type="text" id="lastName" placeholder="Enter your last name" required>

    <label for="age">Age:</label>
    <input type="number" id="age" placeholder="Enter your age" required>

    <label for="email">Email:</label>
    <input type="email" id="email" placeholder="Enter your email" required>

    <label for="username">Username:</label>
    <input type="text" id="username" placeholder="Choose a username" required>

    <label for="dob">Date of Birth:</label>
    <input type="date" id="dob" required>

    <label for="studentClass">Class:</label>
    <select id="studentClass" required>
        <option value="" disabled selected>Select your class</option>
        <option value="class1">Class 1</option>
        <option value="class2">Class 2</option>
        <!-- Add more class options as needed -->
    </select>

    <label for="gender">Gender:</label>
    <select id="gender" required>
        <option value="" disabled selected>Select your gender</option>
        <option value="male">Male</option>
        <option value="female">Female</option>
        <option value="other">Other</option>
    </select>

    <button type="submit">Register</button>
</form>

</body>
</html>
# apps
