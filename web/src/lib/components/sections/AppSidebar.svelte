<script lang="ts">
	import {
		Tooltip,
		TooltipContent,
		TooltipProvider,
		TooltipTrigger,
	} from '$components/feedback';
	import { Slider, Textarea } from '$components/forms';
	import {
		Accordion,
		AccordionContent,
		AccordionItem,
		AccordionTrigger,
		Sidebar,
		SIDEBAR_WIDTH,
		SIDEBAR_WIDTH_MOBILE,
		SidebarContent,
		SidebarFooter,
		SidebarGroup,
		SidebarHeader,
		SidebarProvider,
		SidebarTrigger,
	} from '$components/interactive';
	import { IsMobile } from '$hooks';
	import { Info } from 'lucide-svelte';

	const isMobileHook = new IsMobile();

	let sidebarStates = $state({
		isOpen: !isMobileHook.current,
		isMobile: isMobileHook.current,
		wasAutoOpened: false,
	});

	const triggerLeftPosition = $derived(
		sidebarStates.isOpen
			? sidebarStates.isMobile
				? SIDEBAR_WIDTH_MOBILE
				: SIDEBAR_WIDTH
			: '0rem',
	);

	let { children } = $props();

	$effect(() => {
		const wasMobile = sidebarStates.isMobile;

		sidebarStates.isMobile = isMobileHook.current;

		if (!sidebarStates.isMobile && wasMobile && !sidebarStates.wasAutoOpened) {
			sidebarStates.isOpen = true;
			sidebarStates.wasAutoOpened = true;
		}

		if (sidebarStates.isMobile) {
			if (sidebarStates.isOpen) {
				sidebarStates.isOpen = false;
				return;
			}

			sidebarStates.wasAutoOpened = false;
		}
	});
</script>

<SidebarProvider
	open={sidebarStates.isOpen}
	controlledOpen
	onOpenChange={() => {
		sidebarStates.isOpen = !sidebarStates.isOpen;
		sidebarStates.wasAutoOpened = false;
	}}
>
	<div class="relative">
		<Sidebar>
			<SidebarHeader />
			<SidebarContent>
				<SidebarGroup>
					<Accordion
						type="single"
						value="item-prompt"
					>
						<AccordionItem value="item-prompt">
							<AccordionTrigger
								aria-label="Prompt"
								class="font-bold"
							>
								<span class="flex items-center gap-2">
									Prompt
									<TooltipProvider>
										<Tooltip>
											<TooltipTrigger>
												{#snippet child({ props })}
													<Info
														aria-hidden
														class="stroke-foreground size-3"
														{...props}
													/>
												{/snippet}
											</TooltipTrigger>
											<TooltipContent>
												The description of what you want to see in the image.
											</TooltipContent>
										</Tooltip>
									</TooltipProvider>
								</span>
							</AccordionTrigger>
							<AccordionContent>
								<Textarea
									class="h-28"
									placeholder="e.g. A cat in a hat."
								/>
							</AccordionContent>
						</AccordionItem>
					</Accordion>

					<Accordion
						type="single"
						value="item-negative-prompt"
					>
						<AccordionItem value="item-negative-prompt">
							<AccordionTrigger
								aria-label="Negative Prompt"
								class="font-bold"
							>
								<span class="flex items-center gap-2">
									Negative Prompt
									<TooltipProvider>
										<Tooltip>
											<TooltipTrigger>
												{#snippet child({ props })}
													<Info
														aria-hidden
														class="stroke-foreground size-3"
														{...props}
													/>
												{/snippet}
											</TooltipTrigger>
											<TooltipContent>
												The description of what you DO NOT want to see in the
												image.
											</TooltipContent>
										</Tooltip>
									</TooltipProvider>
								</span>
							</AccordionTrigger>
							<AccordionContent>
								<Textarea
									class="h-28"
									placeholder="Anything you'd like to exclude?"
								/>
							</AccordionContent>
						</AccordionItem>
					</Accordion>

					<Slider
						min={2}
						max={100}
					/>
				</SidebarGroup>
				<SidebarGroup />
			</SidebarContent>
			<SidebarFooter />
		</Sidebar>

		<SidebarTrigger
			class="absolute top-0"
			style={`left:calc(${triggerLeftPosition});`}
		/>
	</div>

	{@render children?.()}
</SidebarProvider>
