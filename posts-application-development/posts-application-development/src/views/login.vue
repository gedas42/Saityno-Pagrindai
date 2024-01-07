<!-- Login.vue -->
<template>
    <main>


        <section class="hero  is-fullheight">
            <div class="hero-body">
              <div class="container">
                <div class="columns is-centered">
                  <div class="column is-5-tablet is-4-desktop is-3-widescreen">
                    <form @submit.prevent="login"  class="box">
                      <div class="field">
                        
                        <label for="name" class="label">Username</label>
                        <div >
                          <input v-model="name" id="name"   placeholder="username" class="input" required>
                          <span class="icon is-small is-left">
                            <i class="fa fa-envelope"></i>
                          </span>
                        </div>
                      </div>
                      <div class="field">
                        <label for="password" class="label">Password</label>
                        <div >
                          <input v-model="password" id="password" type="password" placeholder="*******" class="input" required>
                          <span class="icon is-small is-left">
                            <i class="fa fa-lock"></i>
                          </span>
                        </div>
                        
                      </div>
                      <p>Save information</p>
                      <select name="save" id="save">
                
                        <option value="save">Yes</option>
                        <option value="unsave">No</option>
                      </select>
                      <div class="field">
                        <button type="submit" class="button is-success">
                          Login
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </section>
      </main>

  
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      password: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post(SERVER_ADDR+'/login', {
          name: this.name,
          password: this.password,
        });
        const token = response.data.access_token;
        console.log(token)
        // Store the token in local storage or Vuex state for later use
        localStorage.setItem('access_token', token);
        // Redirect to the protected route

        window.location.href = '/cities';
        
        console.log("logged in")
      } catch (error) {

        console.error(error);
      }
    },
  },
};
</script>