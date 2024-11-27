
async function fetchUserDetails() {
    try {
        const em = localStorage.getItem('email')

        const response = await fetch("/getDetail-forAdmin", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: em }),

        });
        const data = await response.json();
        console.log(data.admin)
        const adminDetailsContainer = document.getElementById("admin-details");
        if (data.admin && data.admin.length > 0) {
    let adminHtml = `
        <table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd;">
            <thead>
                <tr style="background-color: #f2f2f2;">
                    <th style="padding: 8px; text-align: left;">ID</th>
                    <th style="padding: 8px; text-align: left;">Email</th>
                    <th style="padding: 8px; text-align: left;">Password</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding: 8px;">${data.admin[0][0]}</td> 
                    <td style="padding: 8px;">${data.admin[0][1]}</td> 
                    <td style="padding: 8px;">${data.admin[0][2]}</td> 

                </tr>
            </tbody>
        </table>
    `;
    adminDetailsContainer.innerHTML = adminHtml;
} else {
    adminDetailsContainer.innerHTML = "Admin not found.";
}
const userDetailsContainer = document.getElementById("user-details");
if (data.users && data.users.length > 0) {
    let tableHtml = "<table border='1'><tr><th>ID</th><th>Email</th><th>Password</th><th>Role</th><th>Status</th><th>Update</th><th>Delete</th></tr>";
    data.users.forEach(user => {
        tableHtml += `
            <tr>
                <td>${user.id}</td>
                <td>${user.email}</td>
                <td>${user.password}</td>
                <td>${user.role}</td>
                <td>${user.status}</td>
                <td><button id='alter' onclick="updateUserRole(${user.id})">Update</button></td>
                <td><button id='delete' onclick="deleteUserRole(${user.id})">Delete</button></td>
            </tr>
        `;
    });
    tableHtml += "</table>";
    userDetailsContainer.innerHTML = tableHtml;
} else {
    userDetailsContainer.innerHTML = "No users found.";
}

} catch (error) {
    console.error("Error fetching user details:", error);
}
}
fetchUserDetails();

async function deleteUserRole(userId) {
    console.log('deleting')
    const response = await fetch('/deleteUser',{
        method : 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body : JSON.stringify({id : userId})
    });
    const data = await response.json();
    if (data.success) {
        alert("User details updated successfully!");
        fetchUserDetails();
    } else {
        alert("Failed to update user details.");
    }

}

async function updateUserRole(userId) {
    const button = event.target;
    const row = button.parentElement.parentElement; 

    if (button.innerHTML === "Update") {
        button.innerHTML = "Save";

        const emailCell = row.children[1];
        const passwordCell = row.children[2];
        const roleCell = row.children[3];
        const statusSell = row.children[4];

        emailCell.innerHTML = `<input type="text" id="email-${userId}" value="${emailCell.textContent}" />`;
        passwordCell.innerHTML = `<input type="text" id="password-${userId}" value="${passwordCell.textContent}" />`;
        roleCell.innerHTML = `
        <select id="role-${userId}">
            <option value="user" ${roleCell.textContent.trim() === "user" ? "selected" : ""}>User</option>
            <option value="admin" ${roleCell.textContent.trim() === "admin" ? "selected" : ""}>Admin</option>
        </select>`;
        statusSell.innerHTML = `
        <select id="status-${userId}">
            <option value="active" ${statusSell.textContent.trim() === "active" ? "selected" : ""}>active</option>
            <option value="inactive" ${statusSell.textContent.trim() === "inactive" ? "selected" : ""}>inactive</option>
        </select>`;

    } else if (button.innerHTML === "Save") {
        button.innerHTML = "Update";

        const updatedEmail = document.getElementById(`email-${userId}`).value;
        const updatedPassword = document.getElementById(`password-${userId}`).value;
        const updatedRole = document.getElementById(`role-${userId}`).value;
        const updatedStatus = document.getElementById(`status-${userId}`).value;


        try {
            if (updatedRole == 'user') {
                const response = await fetch(`/updateUser`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        id : userId,
                        email: updatedEmail,
                        password: updatedPassword,
                        role: updatedRole,
                        status : updatedStatus
                    })
                });

                const data = await response.json();
                if (data.success) {
                    alert("User details updated successfully!");
                    fetchUserDetails();
                } else {
                    alert("Failed to update user details.");
                }
            }else{
                const response = await fetch(`/addAdmin`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        id : userId,
                        email: updatedEmail,
                        password: updatedPassword,
                    })
                });

                const data = await response.json();
                if (data.success) {
                    alert("User details updated successfully!");
                    fetchUserDetails();
                } else {
                    alert("Failed to update user details.");
                }
            }
        } catch (error) {
            console.error("Error updating user details:", error);
            alert("Error updating user details.");
        }
}
}

const addButton = document.getElementById('addUSer-button');
async function addUser() {
    console.log('adding');
    
    addButton.remove();

    const createButton = document.createElement('button');
    createButton.id = 'create-button';
    createButton.textContent = 'Create';
    createButton.onclick = function() {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const role = document.getElementById('role').value;
        console.log('Create button clicked');
        console.log('Email:', email, 'Password:', password, 'Role:', role);
    };

    const emailInput = document.createElement('input');
    emailInput.type = 'email';
    emailInput.id = 'email';
    emailInput.placeholder = 'Enter email';
    emailInput.required = true;

    const passwordInput = document.createElement('input');
    passwordInput.type = 'password';
    passwordInput.id = 'password';
    passwordInput.placeholder = 'Enter password';
    passwordInput.required = true;

    const roleSelect = document.createElement('select');
    roleSelect.id = 'role';
    roleSelect.required = true;

    const userOption = document.createElement('option');
    userOption.value = 'user';
    userOption.textContent = 'User';
    
    const adminOption = document.createElement('option');
    adminOption.value = 'admin';
    adminOption.textContent = 'Admin';

    roleSelect.appendChild(userOption);
    roleSelect.appendChild(adminOption);

    const formContainer = document.getElementById('form-container'); 
    formContainer.appendChild(emailInput);
    formContainer.appendChild(passwordInput);
    formContainer.appendChild(roleSelect);
    formContainer.appendChild(createButton);

    createButton.addEventListener('click',()=>{
        createUser();
    })
}

async function createUser() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    console.log('Create button clicked');
    console.log('Email:', email, 'Password:', password, 'Role:', role);


        fetch('/addUser', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: email,
                password: password,
                role: role,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('User created successfully!');
                const formContainer = document.getElementById('form-container'); 
                formContainer.innerHTML = '';
                formContainer.appendChild(addButton);

                fetchUserDetails();
            } else {
                alert('Failed to create user.');
            }
        })
    
    .catch(error => {
        console.error('Error creating user:', error);
        alert('Error creating user.');
    });
};
