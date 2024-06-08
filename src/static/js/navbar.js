function generateNavbar() {
    const currentPath = window.location.pathname.split('/').pop();
    const navItems = [
        { name: 'Home', path: 'homepage.html' },
        { name: 'Inventory', path: 'inventory.html' },
        { name: 'Donation', path: 'donation.html' },
        { name: 'Order Now', path: 'transaction.html' },
        { name: 'Log In', path: 'javascript:void(0)', style: 'float: right; padding: 14px 16px;', icon: 'fa fa-user', id: 'loginBtn' }
    ];

    return `
      <div class="topnav">
          ${navItems.map(item => `
            <a href="${item.path}" class="${currentPath === item.path ? 'active' : ''}" ${item.style ? `style="${item.style}"` : ''} ${item.title ? `title="${item.title}"` : ''} ${item.id ? `id="${item.id}"` : ''}>
                ${item.icon ? `<i class="${item.icon}"></i>` : ''} ${item.name}
            </a>
          `).join('')}
          <div class="search-container" style="float: left;">
              <form action="/action_page.php">
                  <input type="text" placeholder="Search.." name="search">
                  <button type="submit"><i class="fa fa-search"></i></button>
              </form>
          </div>
      </div>

      <div id="loginModal" class="modal">
          <div class="modal-content">
              <span class="close">&times;</span>
              <h2>Login</h2>
              <form id="loginForm">
                  <label for="username">Username:</label>
                  <input type="text" id="username" name="username"><br><br>
                  <label for="password">Password:</label>
                  <input type="password" id="password" name="password"><br><br>
                  <button type="submit">Login</button>
              </form>
              <p>Don't have an account? <a href="#" id="signupLink">Sign up</a></p>
          </div>
      </div>

      <div id="signupModal" class="modal">
          <div class="modal-content">
              <span class="close">&times;</span>
              <h2>Sign Up</h2>
              <form id="signupForm">
                  <label for="newUsername">Username:</label>
                  <input type="text" id="newUsername" name="newUsername"><br><br>
                  <label for="newPassword">Password:</label>
                  <input type="password" id="newPassword" name="newPassword"><br><br>
                  <button type="submit">Sign Up</button>
              </form>
          </div>
      </div>
    `;
}

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('navbar').innerHTML = generateNavbar();

    // Get the modals
    var loginModal = document.getElementById("loginModal");
    var signupModal = document.getElementById("signupModal");

    // Get the buttons that open the modals
    var loginBtn = document.getElementById("loginBtn");

    // Get the <span> elements that close the modals
    var closeButtons = document.getElementsByClassName("close");

    // Get the sign up link
    var signupLink = document.getElementById("signupLink");

    // When the user clicks the login button, open the login modal
    loginBtn.onclick = function() {
      loginModal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    for (var i = 0; i < closeButtons.length; i++) {
        closeButtons[i].onclick = function() {
            loginModal.style.display = "none";
            signupModal.style.display = "none";
        }
    }

    // When the user clicks on the sign-up link, open the sign-up modal and close the login modal
    signupLink.onclick = function(event) {
      event.preventDefault();
      loginModal.style.display = "none";
      signupModal.style.display = "block";
    }

    // When the user clicks anywhere outside of the modals, close them
    window.onclick = function(event) {
      if (event.target == loginModal) {
        loginModal.style.display = "none";
      } else if (event.target == signupModal) {
        signupModal.style.display = "none";
      }
    }

    // Add form submission handlers
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();
        window.location.href = 'UserAccount.html';
    });

    document.getElementById('signupForm').addEventListener('submit', function(event) {
        event.preventDefault();
        window.location.href = 'UserAccount.html';
    });
});
