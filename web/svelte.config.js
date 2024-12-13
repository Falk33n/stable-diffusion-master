import adapter from '@sveltejs/adapter-auto';

import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),
	kit: {
		adapter: adapter(),
		alias: {
			$src: './src',
			$routes: './src/routes',
			$lib: './src/lib',
			$server: './src/lib/server',
			$hooks: './src/lib/hooks',
			$components: './src/lib/components',
			$utils: './src/lib/utils',
		},
	},
};
export default config;
