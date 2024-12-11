<script lang="ts">
	import { SidebarProvider, SidebarTrigger } from '$components/interactive';
	import { AppSidebar } from '$components/sections';
	import { H1 } from '$components/typography';

	import '$src/app.css';

	let { children } = $props();
</script>

<SidebarProvider open>
	<AppSidebar />
	<SidebarTrigger />

	<H1>Stable Diffusion</H1>
	<main>
		{@render children?.()}
	</main>
</SidebarProvider>
