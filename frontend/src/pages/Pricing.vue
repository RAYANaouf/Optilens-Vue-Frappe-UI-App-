<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-white shadow">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div>
            <h1 class="text-3xl font-bold text-gray-900">Pricing Management</h1>
            <p class="mt-2 text-gray-600">Manage product pricing and discounts</p>
          </div>
          <Link to="/" class="text-blue-600 hover:text-blue-800 flex items-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
            </svg>
            Back to Dashboard
          </Link>
        </div>
      </div>
    </div>

    <!-- Pricing Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Pricing Rules Section -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <!-- Price Lists -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between mb-4">
            <h2 class="text-xl font-semibold text-gray-900">Price Lists</h2>
            <Button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors text-sm">
              Add Price List
            </Button>
          </div>
          <div class="space-y-3">
            <div class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="font-medium text-gray-900">Standard Price List</h3>
                  <p class="text-sm text-gray-600 mt-1">Default pricing for all customers</p>
                </div>
                <span class="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">Active</span>
              </div>
            </div>
            <div class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="font-medium text-gray-900">Wholesale Price List</h3>
                  <p class="text-sm text-gray-600 mt-1">Special pricing for wholesale customers</p>
                </div>
                <span class="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">Active</span>
              </div>
            </div>
            <div class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="font-medium text-gray-900">Retail Price List</h3>
                  <p class="text-sm text-gray-600 mt-1">Pricing for retail customers</p>
                </div>
                <span class="px-3 py-1 bg-gray-100 text-gray-800 rounded-full text-sm">Inactive</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Discount Rules -->
        <div class="bg-white rounded-lg shadow p-6">
          <div class="flex items-center justify-between mb-4">
            <h2 class="text-xl font-semibold text-gray-900">Discount Rules</h2>
            <Button class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition-colors text-sm">
              Add Discount Rule
            </Button>
          </div>
          <div class="space-y-3">
            <div class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="font-medium text-gray-900">Bulk Discount</h3>
                  <p class="text-sm text-gray-600 mt-1">10% off on orders over $1000</p>
                </div>
                <span class="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">Active</span>
              </div>
            </div>
            <div class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="font-medium text-gray-900">Seasonal Discount</h3>
                  <p class="text-sm text-gray-600 mt-1">15% off on selected items</p>
                </div>
                <span class="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">Active</span>
              </div>
            </div>
            <div class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="font-medium text-gray-900">Customer Loyalty</h3>
                  <p class="text-sm text-gray-600 mt-1">5% off for loyal customers</p>
                </div>
                <span class="px-3 py-1 bg-gray-100 text-gray-800 rounded-full text-sm">Inactive</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Product Pricing Table -->
      <div class="bg-white rounded-lg shadow">
        <div class="p-6 border-b">
          <div class="flex items-center justify-between">
            <h2 class="text-xl font-semibold text-gray-900">Product Pricing</h2>
            <div class="flex gap-2">
              <Button class="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-200 transition-colors">
                Import Prices
              </Button>
              <Button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
                Update Prices
              </Button>
            </div>
          </div>
          <div class="mt-4 flex gap-4">
            <input
              type="text"
              placeholder="Search products..."
              class="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
            <select class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
              <option>All Price Lists</option>
              <option>Standard</option>
              <option>Wholesale</option>
              <option>Retail</option>
            </select>
          </div>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Item Code</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Item Name</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Standard Price</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Wholesale Price</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Last Updated</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-if="$resources.pricing.loading">
                <td colspan="6" class="px-6 py-12 text-center text-gray-500">
                  <p class="text-lg font-medium">Loading pricing data...</p>
                </td>
              </tr>
              <tr v-else-if="!$resources.pricing.data || $resources.pricing.data.length === 0">
                <td colspan="6" class="px-6 py-12 text-center text-gray-500">
                  <svg class="w-16 h-16 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  <p class="text-lg font-medium">No pricing data found</p>
                  <p class="text-sm mt-1">Add products to manage their pricing</p>
                </td>
              </tr>
              <tr v-else v-for="item in filteredPricing" :key="item.item_code">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ item.item_code }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ item.item_name }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ formatCurrency(item.standard_rate) }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ formatCurrency(item.wholesale_rate) }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatDate(item.modified) }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  <button class="text-blue-600 hover:text-blue-900">Edit</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Pricing',
  data() {
    return {
      searchQuery: '',
      selectedPriceList: 'All',
    }
  },
  resources: {
    pricing: {
      url: 'optilens_vue.api.get_pricing_data',
      auto: true,
    },
  },
  computed: {
    filteredPricing() {
      if (!this.$resources.pricing.data) return []
      return this.$resources.pricing.data.filter(item => {
        const matchesSearch = 
          item.item_name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          item.item_code.toLowerCase().includes(this.searchQuery.toLowerCase())
        return matchesSearch
      })
    },
  },
  methods: {
    formatCurrency(amount) {
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
      }).format(amount || 0)
    },
    formatDate(dateString) {
      if (!dateString) return '-'
      return new Date(dateString).toLocaleDateString()
    },
  },
}
</script>
