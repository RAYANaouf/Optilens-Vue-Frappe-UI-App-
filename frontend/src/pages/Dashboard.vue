<template>
  <div class="min-h-screen bg-gray-50 flex flex-col">
    <!-- Header -->
    <div class="bg-white shadow">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <h1 class="text-3xl font-bold text-gray-900">Optilens Dashboard</h1>
      </div>
    </div>

    <!-- Dashboard Cards -->
    <div class="flex-1 flex items-center justify-center px-4">
      <div class="max-w-4xl w-full">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- POS Card -->
        <Link
          to="/pos"
          class="bg-white rounded-lg border border-gray-200 hover:border-blue-500 transition-all duration-300 p-8 flex flex-col items-center justify-center text-center"
        >
          <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-4">
            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-900">Point of Sale</h3>
          <p class="mt-2 text-gray-600">Manage sales and transactions</p>
        </Link>

        <!-- Stock Card -->
        <Link
          to="/stock"
          class="bg-white rounded-lg border border-gray-200 hover:border-green-500 transition-all duration-300 p-8 flex flex-col items-center justify-center text-center"
        >
          <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mb-4">
            <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-900">Stock Management</h3>
          <p class="mt-2 text-gray-600">Track inventory and stock levels</p>
        </Link>

        <!-- Pricing Card -->
        <Link
          to="/pricing"
          class="bg-white rounded-lg border border-gray-200 hover:border-purple-500 transition-all duration-300 p-8 flex flex-col items-center justify-center text-center"
        >
          <div class="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mb-4">
            <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-900">Pricing</h3>
          <p class="mt-2 text-gray-600">Manage product pricing and discounts</p>
        </Link>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Link } from 'frappe-ui'

export default {
  name: 'Dashboard',
  components: {
    Link,
  },
}
</script>
