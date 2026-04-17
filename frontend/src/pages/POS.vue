<template>
  <div class="min-h-screen bg-gray-50 flex">
    <!-- Sidebar Backdrop -->
    <div
      @click="sidebarOpen = false"
      class="fixed inset-0 bg-black bg-opacity-50 z-50 transition-opacity duration-300"
      :class="{ 'opacity-0 pointer-events-none': !sidebarOpen, 'opacity-100 pointer-events-auto': sidebarOpen }"
    ></div>

    <!-- Sidebar -->
    <div
      class="fixed top-0 left-0 h-full w-64 bg-white shadow-2xl z-50 transition-all duration-500 ease-out"
      :class="{ '-translate-x-full': !sidebarOpen, 'translate-x-0': sidebarOpen }"
    >
        <div class="p-4">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-xl font-bold text-gray-900">Menu</h2>
          <button
            @click="sidebarOpen = false"
            class="text-gray-500 hover:text-gray-700"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        <nav class="space-y-2">
          <Link
            to="/"
            class="flex items-center px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
            </svg>
            Dashboard
          </Link>
          <Link
            to="/stock"
            class="flex items-center px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
            </svg>
            Stock
          </Link>
          <Link
            to="/pricing"
            class="flex items-center px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            Pricing
          </Link>
        </nav>
      </div>
    </div>

    <!-- Main Content -->
    <div class="flex-1 p-4">
      <!-- POS Content -->
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="flex justify-between items-center mb-4">
          <!-- Sidebar Toggle Button -->
          <button
            @click="sidebarOpen = !sidebarOpen"
            class="bg-blue-600 text-white px-4 py-2 rounded-lg shadow-lg hover:bg-blue-700 transition-colors flex items-center"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
            Menu
          </button>
          <!-- Exit Button -->
          <Link
            to="/"
            class="bg-gray-600 text-white px-4 py-2 rounded-lg shadow-lg hover:bg-gray-700 transition-colors flex items-center"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
            </svg>
            Exit
          </Link>
        </div>
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Products Section -->
        <div class="lg:col-span-2">
          <div class="bg-white rounded-lg shadow p-6">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Products</h2>
            <div class="mb-4">
              <input
                type="text"
                v-model="searchQuery"
                placeholder="Search products..."
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
            <div v-if="$resources.products.loading" class="text-center py-8">
              <p class="text-gray-600">Loading products...</p>
            </div>
            <div v-else class="grid grid-cols-2 md:grid-cols-3 gap-4">
              <div
                v-for="product in filteredProducts"
                :key="product.item_code"
                class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer"
                @click="addToCart(product)"
              >
                <div class="h-32 bg-gray-100 rounded-lg mb-3 flex items-center justify-center">
                  <img v-if="product.image" :src="product.image" class="w-full h-full object-cover rounded-lg" />
                  <svg v-else class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                  </svg>
                </div>
                <h3 class="font-medium text-gray-900">{{ product.item_name }}</h3>
                <p class="text-gray-600 text-sm">{{ formatCurrency(product.standard_rate) }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Cart Section -->
        <div class="lg:col-span-1">
          <div class="bg-white rounded-lg shadow p-6 sticky top-6">
            <h2 class="text-xl font-semibold text-gray-900 mb-4">Current Sale</h2>
            <div class="space-y-3 mb-4">
              <div v-if="cart.length === 0" class="text-center py-8 text-gray-500">
                <svg class="w-12 h-12 mx-auto text-gray-300 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
                <p>No items in cart</p>
              </div>
              <div v-else>
                <div
                  v-for="item in cart"
                  :key="item.item_code"
                  class="flex items-center justify-between p-3 bg-gray-50 rounded-lg"
                >
                  <div class="flex-1">
                    <h4 class="font-medium text-gray-900">{{ item.item_name }}</h4>
                    <p class="text-sm text-gray-600">{{ formatCurrency(item.price) }} x {{ item.qty }}</p>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="font-semibold">{{ formatCurrency(item.price * item.qty) }}</span>
                    <button
                      @click="removeFromCart(item.item_code)"
                      class="text-red-600 hover:text-red-800"
                    >
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="border-t pt-4">
              <div class="flex justify-between text-lg font-semibold">
                <span>Total:</span>
                <span>{{ formatCurrency(cartTotal) }}</span>
              </div>
              <Button
                class="w-full mt-4 bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition-colors font-medium"
              >
                Complete Sale
              </Button>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'POS',
  data() {
    return {
      searchQuery: '',
      cart: [],
      sidebarOpen: false,
    }
  },
  resources: {
    products: {
      url: 'optilens_vue.api.get_pos_products',
      auto: true,
      onError: (error) => {
        console.error('Error loading products:', error)
      },
    },
  },
  computed: {
    filteredProducts() {
      if (!this.$resources.products.data) return []
      const query = this.searchQuery.toLowerCase()
      return this.$resources.products.data.filter(product => {
        const name = product.item_name || product.name || ''
        const code = product.item_code || product.code || ''
        return name.toLowerCase().includes(query) || code.toLowerCase().includes(query)
      })
    },
    cartTotal() {
      return this.cart.reduce((total, item) => total + (item.price * item.qty), 0)
    },
  },
  methods: {
    formatCurrency(amount) {
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
      }).format(amount || 0)
    },
    addToCart(product) {
      const existingItem = this.cart.find(item => item.item_code === product.item_code)
      if (existingItem) {
        existingItem.qty++
      } else {
        this.cart.push({
          item_code: product.item_code,
          item_name: product.item_name,
          price: product.standard_rate,
          qty: 1,
        })
      }
    },
    removeFromCart(itemCode) {
      const index = this.cart.findIndex(item => item.item_code === itemCode)
      if (index > -1) {
        this.cart.splice(index, 1)
      }
    },
  },
}
</script>
