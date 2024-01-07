<template>
    <nav
        class="navbar is-light px-6"
        role="navigation"
        aria-label="main navigation"
        :class="{ 'is-active': isNavOpen }"
    >
        <div class="navbar-brand">
            <a
                role="button"
                class="navbar-burger"
                aria-label="menu"
                aria-expanded="false"
                data-target="navbarBasicExample"
                @click="toggleNav"
            >
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div class="navbar-menu">
            <div class="navbar-start">
                <router-link style="font-family: 'alex_brushregular'" to="/" class="navbar-item" >Home</router-link>
                
                <router-link to="/cities" class="navbar-item" style="font-family: 'alex_brushregular'">
                    Cities
                </router-link>
                <div class="navbar-item has-dropdown is-hoverable">

    
                    <div class="navbar-dropdown">
                      <hr class="navbar-divider">
                    
                    </div>
                  </div>
                </div>

                    <router-link v-if="!isTokenSet" to="/login" class="navbar-item" style="allign-right">Login</router-link>
                

                <div class="navbar-item has-dropdown is-hoverable">

    
                    <div class="navbar-dropdown">
                      <hr class="navbar-divider">
                    
                    </div>
                  </div>
                </div>
            
                <div class="navbar-end" style="alingn:right">
                  <div v-if="isTokenSet" class="navbar-item has-dropdown is-hoverable">
                    <a v-if="isTokenSet" class="navbar-link">
                      Paskyra
                    </a>
            
                    <div v-if="isTokenSet" class="navbar-dropdown">
                      
                   
        
                       
          
                      <hr class="navbar-divider">
                      <a v-if="isTokenSet" class="navbar-item"
                        @click="logout"
                      >
                      Atsijungti
                    </a>
                    </div>
                  </div>
            </div>

    </nav>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            isNavOpen: false,
        };
    },
    methods: {
        toggleNav() {
            this.isNavOpen = !this.isNavOpen;
        },
        async logout() {
      try {
        await axios.post(SERVER_ADDR+'/logout');
        // Clear the JWT token from local storage or cookies
        localStorage.removeItem('access_token');
   
        // Redirect the user to the login page or perform any other action
        window.location.href = '/login';
        
      } catch (error) {
        console.error(error);
      }
    },

    },
    computed: {
    isTokenSet() {
      // Check if the token is set in local storage or cookies
      this.$forceUpdate()
      return localStorage.getItem('access_token') !== null;
    },
    
     decodeJwt(token) {
     const base64Url = localStorage.getItem('access_token').split('.')[1];
     const base64 = base64Url.replace('-', '+').replace('_', '/');
      console.log(JSON.parse(atob(base64)))
}
  },
};

</script>

<style>
@media screen and (max-width: 1023px) {
    .navbar-menu {
        display: none;
    }
    .navbar.is-active .navbar-menu {
        display: block;
        position: absolute;
        left: 0;
        right: 0;
        padding: 0;
    }
    .navbar.is-active .navbar-menu a {
        text-align: center;
    }
}


@font-face {
  font-family: 'alex_brushregular';
  src: url('../webfontkit-20231218-031635/alexbrush-regular.woff2') format('woff2'),
       url('../webfontkit-20231218-031635/alexbrush-regular.woff') format('woff');
  font-weight: normal;
  font-style: normal;

}
</style>
