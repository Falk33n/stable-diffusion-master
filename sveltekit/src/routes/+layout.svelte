<script lang="ts">
	import { SidebarProvider, SidebarTrigger } from '$components/interactive';
	import { AppSidebar } from '$components/sections';

	import '$src/app.css';

	let { children } = $props();
</script>

<SidebarProvider>
	<AppSidebar />
	<main>
		<SidebarTrigger />
		{@render children?.()}
	</main>
</SidebarProvider>
